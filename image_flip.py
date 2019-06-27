import setup
import os
from PIL import Image


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

        # Place holder for the flipped image
        flipped_img = Image.new("RGB", orig_img.size)

        for y in range(0, orig_height):
            i = 0
            for x in range(orig_width - 1, -1, -1):
                curr_pixel = orig_img.getpixel((x, y))
                flipped_img.putpixel((i, y), curr_pixel)
                i = i + 1

        flipped_file_name = "flipped_" + file_name + file_extension

        flipped_img.save(flipped_file_name)
    except Exception as err:
        print(err)


flip_image("sample1.jpg")
