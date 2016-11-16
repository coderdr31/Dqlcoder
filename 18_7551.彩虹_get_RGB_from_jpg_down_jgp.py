#!/usr/bin/python
# coding: utf-8
# 那么问题来了,下面这张图片是一张纯色图片。这题的答案就是这张图片色彩的RGB值。

# 方法一: Chrome
# F2 -> Element -> Style -> 添加: color: red; -> 点击左侧的小方块, Color pick -> Shift + 左键去选取

# 方法二: python

from PIL import Image
import os

url = "http://www.qlcoder.com/uploads/61244.jpg"
filename = "18_7551.jpg"

if not os.path.isfile(filename):
    print "下载数据"
    import requests

    # 两种方法得到图片
    # 第一种
    # with open(filename, "wb") as f:
    #     response = requests.get(url, stream = True)
    #     if not response.ok:
    #         print "download error"
    #     for block in response.iter_content(1024):
    #         f.write(block)

    # 第二种
    r = requests.get(url)
    with open(filename, "wb") as f:
        f.write(r.content)

image = Image.open(filename)
pixel = image.load()
r, g, b = pixel[0, 0]
print r, g, b
