import os, shutil
from PIL import Image


COLORS = {
    'red': '\033[31m',
    'green': '\033[32m',
    'orange': '\033[33m',
    'blue': '\033[34m'
}


def color_print(text, color):
    ''' Print text with specified color '''
    code = COLORS.get(color, '')
    print(code, text, '\033[0m')


def scan_media(path):
    ''' Function that checks and finds all 
    image files in a directory. Then
    it stores all image filenames in a list. In this case,
    all non-image files are considered as videos '''

    filenames = os.listdir(path)
    images = []
    videos = []

    for filename in filenames:
        try:
            image = Image.open(
                os.path.join(path, filename)
            )
        except:
            videos.append(filename)
        else:
            images.append(filename)
            image.close()

    color_print(
        f'სულ ნაპოვნია {len(images)} ფოტო და {len(videos)} ვიდეო. მუშავდება...', 'blue'
        )

    return images, videos


def remove_directories(*paths):
    ''' removes all directories by path passed as an argument '''
    color_print('იშლება ფაილები ლოკალურად...', 'blue')

    for path in paths:
        shutil.rmtree(path, ignore_errors=True)

    color_print('პროცესი დასრულებულია!', 'green')