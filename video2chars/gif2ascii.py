#   _*_ coding:utf-8 _*_
 
from PIL import Image, ImageSequence, ImageDraw, ImageFont
import argparse
import numpy as np

sample_rate = 0.4
np.set_printoptions(threshold=np.inf)

def ascii_art(im_obj):
    im = im_obj
    im = im.convert('RGB')

    # Compute letter aspect ratio
    font = ImageFont.load_default()
    # font = ImageFont.truetype("SourceCodePro-Bold.ttf", size=12)
    aspect_ratio = font.getsize("x")[0] / font.getsize("x")[1]
    new_im_size = np.array(
        [im.size[0] * sample_rate, im.size[1] * sample_rate * aspect_ratio]
    ).astype(int)

    # Downsample the image
    im = im.resize(new_im_size)

    # Keep a copy of image for color sampling
    im_color = np.array(im)

    # Convert to gray scale image
    im = im.convert("L")

    # Convert to numpy array for image manipulation
    im = np.array(im)

    # Defines all the symbols in ascending order that will form the final ascii
    symbols = np.array(list(" .-vM"))

    # Normalize minimum and maximum to [0, max_symbol_index)
    im = (im - im.min()) / (im.max() - im.min()) * (symbols.size - 1)

    # Generate the ascii art
    ascii = symbols[im.astype(int)]

    # Create an output image for drawing ascii text
    letter_size = font.getsize("x")
    im_out_size = new_im_size * letter_size
    bg_color = "black"
    im_out = Image.new("RGB", tuple(im_out_size), bg_color)
    draw = ImageDraw.Draw(im_out)

    # Draw text
    y = 0
    for i, line in enumerate(ascii):
        for j, ch in enumerate(line):
            color = tuple(im_color[i, j])  # sample color from original image
            draw.text((letter_size[0] * j, y), ch[0], fill=color, font=font)
        y += letter_size[1]  # increase y by letter height
	
    return im_out

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert any image to ascii art.")
    parser.add_argument(
        "file", type=str, help="input image file",
    )
    args = parser.parse_args()
    im = Image.open(args.file)
    #   初始化列表
    sequence = []
    for f in ImageSequence.Iterator(im):
        #   获取图像序列并存储
        sequence.append(ascii_art(f))
        #   将图像序列逆转
    sequence[0].save('out.gif', save_all=True, append_images=sequence[1:])


