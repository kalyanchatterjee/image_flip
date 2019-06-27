import setup
from PIL import Image
import os


def flip_image(image_path):
    try:
        # Create a new Image object
        orig_img = Image.open(image_path)

        file_props = os.path.splitext(image_path)
        file_name = file_props[0]
        file_extension = file_props[1]

        # Get the dimensions of the original image
        size = orig_img.size
        orig_width = size[0]
        orig_height = size[1]

        for y in range(0, orig_height):
            # Only going up to half the width
            for x in range(0, orig_width//2):
                pixel1 = orig_img.getpixel((x, y))
                pixel2 = orig_img.getpixel((orig_width - x - 1, y))

                orig_img.putpixel((x, y), pixel2)
                orig_img.putpixel((orig_width - x - 1, y), pixel1)

        orig_img.save(file_name + file_extension)
    except Exception as err:
        print(err)


flip_image('sample1.jpg')
