import os
from moviepy.config import change_settings

# platform dependant config
if os.name == 'nt':
    # specify imagemagick binary path (required on windows)
    change_settings({
        "IMAGEMAGICK_BINARY": r"C:\Program Files\ImageMagick-7.1.0-Q16-HDRI\magick.exe"
    })


class Paths:
    BASE_DIR = os.getcwd()
    TARGET_PATH = os.path.join(BASE_DIR, 'Transfer') 
    RESULT_PATH = os.path.join(BASE_DIR, 'Processed')
    RESOURCES_PATH = os.path.join(BASE_DIR, 'resources')

    MUSIC_PATH = os.path.join(RESOURCES_PATH, 'music')
    FONT_PATH = os.path.join(RESOURCES_PATH, 'font.ttf')

    ANDROID_TARGET_MEDIA_PATH = "storage/self/primary/DCIM/Transfer/"
    ANDROID_PROCESSED_MEDIA_PATH = "storage/self/primary/DCIM/Processed/"

    LOCAL_TARGET_MEDIA_PATH = BASE_DIR
    LOCAL_PROCESSED_MEDIA_PATH = os.path.join(RESULT_PATH, '*')

    ADB_SHELL_PATH = os.path.join(RESOURCES_PATH, 'platform-tools', 'adb')

    # Also edit line 30 in media_transfer.py.

class ImageConf:
    text = "Lorem Ipsum ;)"
    text_color = 'black'
    text_stroke_fill = 'white'
    text_stroke_weight = 2
    text_width_fraction = 0.3
    text_pos = (50, 70)


class VideoConf:
    text = "Lorem Ipsum ;)"
    text_pos = 'bottom'
    text_color = 'white'
    fps = 30
    threads = 8
    codec='mpeg4'
    compress=True
