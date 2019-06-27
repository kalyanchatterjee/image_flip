import setup
from PIL import Image, ImageDraw
import os


def flip_image(image_path):
    try:
        # Create a new Image object
        orig_img = Image.open(image_path)

        file_props = os.path.splitext(image_path)
        file_name = file_props[0]
        file_extension = file_props[1]

        # Place holder for the flipped image
        flipped_img = Image.new("RGB", orig_img.size)
        # https://pillow.readthedocs.io/en/3.1.x/reference/ImageDraw.html
        draw = ImageDraw.Draw(flipped_img)

        # Flipped image props
        flipped_height = flipped_img.height
        flipped_width = flipped_img.width

        for y in range(0, flipped_height):
            for x in range(0, flipped_width):
                new_x = orig_img.width - x - 1
                draw.point((x, y), orig_img.getpixel((new_x, y)))

        flipped_file_name = "flipped_" + file_name + file_extension
        flipped_img.save(flipped_file_name)
    except Exception as err:
        print(err)


flip_image('sample1.jpg')
