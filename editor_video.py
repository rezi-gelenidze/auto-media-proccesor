import os, random
from moviepy.editor import *

from helpers import color_print
from settings import VideoConf, Paths


def process_videos(video_filenames):
    color_print('იწყება ვიდეოების დამუშავება', 'blue')

    # get lists of music playlist and target videos
    music_files = os.listdir(Paths.MUSIC_PATH)

    total = len(video_filenames)
    current = 1

    for video_name in video_filenames:
        color_print(f'მუშავდება ვიდეო [{current}/{total}]', 'blue')

        # get current target video path
        video_path = os.path.join(Paths.TARGET_PATH, video_name)

        # randomly choose audio file
        audio_path = os.path.join(Paths.MUSIC_PATH, random.choice(music_files))

        # load video and audio file
        video = VideoFileClip(video_path)
        audio = AudioFileClip(audio_path)

        # extend or trim audio to video duration [cool solution ;)]
        if video.duration > audio.duration:
            audio = audio.audio_loop(duration=video.duration)
        else:
            audio = audio.set_duration(video.duration)

        # change audio
        video.audio = audio

        # converting video to 720 if needed
        if VideoConf.compress:
            vh, vw = video.size

            if vh > vw and vh > 720:
                video = video.resize(height=720)
            elif vw > vh and vw > 720:
                video = video.resize(width=720)

        # calculate text size
        vh, vw = video.size    

        tw = vw * 0.4
        th = vh * 0.1

        # Generate a text clip 
        txt_clip = TextClip(
            txt=VideoConf.text,
            size=(tw,th),
            color=VideoConf.text_color, 
        )
        
        txt_clip = txt_clip \
            .set_position(VideoConf.text_pos) \
            .set_duration(video.duration)

        # set new audio and write text
        new_video = CompositeVideoClip([video, txt_clip])

        # save
        new_video.write_videofile(
            os.path.join(Paths.RESULT_PATH, video_name),
            fps=VideoConf.fps,
            codec=VideoConf.codec,
            threads=VideoConf.threads
        )
        video.close()

        # increment counter
        current += 1