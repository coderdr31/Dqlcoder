#!/usr/bin/python
# coding: utf-8

# 在这里我介绍1种最简单的隐写术:基于rgb分量的最低位的隐写术。
# 这题的答案在该lenna图片的红色分量上。

from PIL import Image
import os

fileurl = "http://121.201.63.168/uploads/145303100168558.png"
filename = "84_7617.png"

if not os.path.isfile(filename):
    print "download file"
    import requests
    with open(filename, "wb") as f:
        f.write(requests.get(fileurl).content)

im = Image.open(filename)
r, g, b = im.split()
out = r.point(lambda i: (i % 2 == 0) * 200)
out.show()

