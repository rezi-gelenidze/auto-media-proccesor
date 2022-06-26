from media_transfer import fetch_media, transfer_media
from editor_image import process_images
from editor_video import process_videos
from helpers import scan_media, remove_directories

from settings import Paths


def main():
    # clear media directories locally if it is left on previous run
    remove_directories(Paths.TARGET_PATH, Paths.RESULT_PATH)
    
    # Fetch target media from android device
    fetch_media() 

    # Organize media filenames in two lists
    images, videos = scan_media(Paths.TARGET_PATH)

    # process images, then videos
    process_images(images) 
    process_videos(videos)

    # transfer processed media back to android device
    transfer_media()

    # clear media directories locally
    remove_directories(Paths.TARGET_PATH, Paths.RESULT_PATH)


if __name__ == "__main__":
    main()