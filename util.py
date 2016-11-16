#!/usr/bin/python
# coding: utf-8

import os
import requests


def loadfile(url, filename):
    '确保文件已经下载'
    if not os.path.isfile(filename):
        print('下载文件……')
        r = requests.get(url)
        with open(filename, 'wb') as f:
            f.write(r.content)
            print('下载完成', filename)
    else:
        print('文件早已准备好。', filename)
