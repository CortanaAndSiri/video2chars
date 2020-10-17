# Video to Chars

[![Build Status](https://travis-ci.org/ryan4yin/video2chars.svg?branch=master)](https://travis-ci.org/ryan4yin/video2chars)
[![PYPI Version](https://img.shields.io/pypi/v/video2chars.svg)](https://pypi.org/project/video2chars/)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/07055fe560ba40af83ec09d413d93f4c)](https://app.codacy.com/app/xiaoyin_c/video2chars?utm_source=github.com&utm_medium=referral&utm_content=ryan4yin/video2chars&utm_campaign=Badge_Grade_Dashboard)
[![Python 3.6+](https://img.shields.io/pypi/pyversions/video2chars.svg?style=flat)](https://www.python.org/)

Convert video to character art animation.

Strictly speaking, this project is an optimized version of the merger of two small projects. Because it is very interesting, I compared multiple pieces of code. It was changed under the code of the two  guys in pronhgithub. The core code of the two  guys was used to fix Some bugs, stitched and assembled:
The screen processing is character animation core code using most of the code of rossning92 (ascii_art.py) (two bugs were fixed at the same time, [original url](https://gist.github.com/rossning92/bb1667e5e14a63148dcd61b4455ce52f)
Video and audio processing is most of the code of ryan4yin boss video2chars (parts deleted, [original url](https://github.com/ryan4yin/video2chars)
This is a command line tool that can convert pictures and video files into character animations, using pillow + moviepy to achieve

[中文说明](/doc/README-zh-cn.md)


## Usage

```
python video2chars.py [--help --fps INTEGER --t_start  INTEGER --t_end INTEGER --output TEXT] FILENAME

Usage: converter.py [OPTIONS] FILENAME

Options:
  --fps INTEGER      frames per second, default to 16
  --t_start INTEGER  the start time that the video needs to be converted(in
                     seconds)
  --t_end INTEGER    the end time that the video needs to be converted(in
                     seconds)
  --output TEXT      output to a file with this name, default to "output.mp4"
  --help             Show this message and exit.

Example
	python video2chars.py --fps 30  --t_start 0  --t_end 10 --output output.mp4  inputfile.mp4
```
The command shows that the specified video will be converted to an ascii art animation with 30 fps, and only convert the first 10 seconds. 
you'll see a file named `output.mp4` in your current directory when completes, have fun ~

>p.s. it's a bit slow, turn down the width and fps, to speed up the conversion. 

Check `video2chars --help` for more information.

```
python video2ascii.py  FILENAME

Example
	 python video2ascii.py test.jpg
```
Convert a picture to a character picture


```
python gif2ascii.py  FILENAME

Example
	 python video2ascii.py test.gif
```
Convert a gif picture to a character gif picture

## Code Reference
-[Screen processing (version rossning92)] The core code for the image processing is character animation. Most of the code (ascii_art.py) used by rossning92 is used (two bugs fixed at the same time, [original url](https://gist.github.com/rossning92/bb1667e5e14a63148dcd61b4455ce52f)
-[Audio and video processing (ryan4yin version)] Video and audio processing is most of the code of ryan4yin boss video2chars (parts deleted, [original url](https://github.com/ryan4yin/video2chars)



## Related Projects

- [Video2ASCII.jl(Julia Version)](https://github.com/ryan4yin/Video2ASCII.jl)


