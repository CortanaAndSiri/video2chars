# 视频转字符动画

[![Build Status](https://travis-ci.org/ryan4yin/video2chars.svg?branch=master)](https://travis-ci.org/ryan4yin/video2chars)
[![PYPI Version](https://img.shields.io/pypi/v/video2chars.svg)](https://pypi.org/project/video2chars/)
[![Python 3.6+](https://img.shields.io/pypi/pyversions/video2chars.svg?style=flat)](https://www.python.org/)

该项目严格意义上来说是两个小项目合并的优化版本,因为比较感兴趣，对比了多段代码，在pronhub两个大佬的代码下改动完成的，使用两位大佬的核心代码，填补了一些bug，缝合拼装完成：
	画面处理为字符动画核心代码使用为rossning92大佬的大部分代码(ascii_art.py)（同时修补了两处bug,[原url](https://gist.github.com/rossning92/bb1667e5e14a63148dcd61b4455ce52f)
	视频音频处理为ryan4yin大佬的大部分代码video2chars(删减了部分，[原url](https://github.com/ryan4yin/video2chars)
这是一个能将图片，视频文件转换成字符动画的命令行工具，使用 pillow + moviepy 实现

## 安装


因为本工具依赖 `imageio-ffmpeg`，但只有二进制版本的该依赖内嵌 ffmpeg，如果你从源码安装，很可能会出问题。

## 代码参考
- [画面处理(rossning92版本)] 画面处理为字符动画核心代码使用为rossning92大佬的大部分代码(ascii_art.py)（同时修补了两处bug,[原url](https://gist.github.com/rossning92/bb1667e5e14a63148dcd61b4455ce52f)
- [音频视频处理(ryan4yin版本)]视频音频处理为ryan4yin大佬的大部分代码video2chars(删减了部分，[原url](https://github.com/ryan4yin/video2chars)

## 用法

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
上面的命令表示，将指定路径的视频，转换成fps为30的视频，只转换前十秒。
命令运行完毕后，会在当前目录下生成一个名为 `output.mp4` 的字符视频。

使用 `video2chars --help` 命令，获取更多信息。

```
python video2ascii.py  FILENAME

Example
	 python video2ascii.py test.jpg
```
单张图片转换为字符图片

>p.s. 注意性能，python 单核跑的，慢也没办法。实在是慢的话，可以尝试调低一下这两个参数。


```
python gif2ascii.py  FILENAME

Example
   python video2ascii.py test.gif
```
将gif处理为字符gif图



## 相关项目

- [Video2ASCII.jl(Julia 版)](https://github.com/ryan4yin/Video2ASCII.jl)
