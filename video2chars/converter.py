# -*- coding:utf-8 -*-

from pkg_resources import resource_stream
import numpy as np
from moviepy.editor import *
from PIL import Image, ImageFont, ImageDraw
import click


class Video2Chars:
    def __init__(self, video_path, fps, t_start=0, t_end=None):
        """
        :param video_path: 字符串, 视频文件的路径
        :param fps: 生成的视频的帧率
        :param chars_width: 字符的宽度（以像素记），会影响最终视频的分辨率。
        :param t_start, t_end: 视频的开始时间和结束时间，只处理指定时间段的视频。
        """
        # 加载视频,并截取
        self.video_clip = VideoFileClip(video_path).subclip(t_start, t_end)
        self.fps = fps

    def get_chars_frame(self, t):
        """将图片转换为字符画"""
        # 获取到图像
        sample_rate = 0.4

        img_np = self.video_clip.get_frame(t)
        im = Image.fromarray(img_np, "RGB")

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
        symbols = np.array(list(" .-ovDGMM"))

        # Normalize minimum and maximum to [0, max_symbol_index)
        if im.min() == im.max() :
            im = (im)/ 255 * (symbols.size - 1)
        else:
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
        self.video_size = int(im_out.width),int(im_out.height)
        return np.array(im_out)

    def generate_chars_video(self):
        """生成字符视频对象"""
        clip = VideoClip(self.get_chars_frame,duration=self.video_clip.duration)

        return (clip.set_fps(self.fps)
                .set_audio(self.video_clip.audio))


@click.command()
@click.option("--fps", default=16, help='frames per second, default to 16')
@click.option("--t_start", default=0, help="the start time that the video needs to be converted(in seconds)")
@click.option("--t_end", default=None, type=int, help="the end time that the video needs to be converted(in seconds)")
@click.option("--output", default="output.mp4", help='output to a file with this name, default to "output.mp4"')
@click.argument("filename")
def convert(filename, fps, output, t_start, t_end):
    converter = Video2Chars(video_path=filename,
                            fps=fps,
                            t_start=t_start,
                            t_end=t_end
                            )

    clip = converter.generate_chars_video()
    clip.write_videofile(output)


if __name__ == '__main__':
    convert()
