from PIL import Image, ImageFont, ImageDraw  
import os

from helpers import color_print
from settings import ImageConf, Paths


def get_font_size(image_width):
    # Calculate font size of text
    target_width = image_width * ImageConf.text_width_fraction
    font_size = 1  # starting font size

    # Increment font size before it fits target width fraction of image
    font = ImageFont.truetype(Paths.FONT_PATH, font_size)
    
    while font.getsize(ImageConf.text)[0] < target_width:
        font_size += 1 # Increment font size for next iteration
        font = ImageFont.truetype(Paths.FONT_PATH, font_size)

    # De-increment to get target width
    return font_size - 1


def write_text(img):
    iW, iH = img.size
    draw = ImageDraw.Draw(img)

    # Calculate and set font size
    font_size = get_font_size(iW)
    font = ImageFont.truetype(Paths.FONT_PATH, font_size)

    # Calculate text position over image
    tW, tH = draw.textsize(ImageConf.text, font=font)
    posX, posY = ImageConf.text_pos

    pos = (
        int((iW-tW) / 100 * posX), int((iH-tH) / 100 * posY)
        )

    # Draw text
    draw.text(
        pos,
        ImageConf.text,
        font=font,
        fill=ImageConf.text_color,
        stroke_fill=ImageConf.text_stroke_fill,
        stroke_width=ImageConf.text_stroke_weight
    )  


def process_images(image_filenames):
    color_print('იწყება ფოტოების დამუშავება', 'blue')
    if 'Processed' not in os.listdir():
        os.mkdir('Processed')
    
    # add text on all images
    for img_name in image_filenames:
        image = Image.open(
            os.path.join(Paths.TARGET_PATH, img_name)
            )
        
        write_text(image)
        
        # save image file
        image.save(
            os.path.join(Paths.RESULT_PATH, img_name)
            )

    color_print('ფოტოების დამუშავება დასრულებულია!', 'green')


if __name__ == '__main__':
    process_images()
