# !/usr/bin/python
# coding: utf-8
# 这里有一个大小为100G的文件，答案在该文件的第12345678901Byte至12345678999Byte，千万不要从头开始下载哦。
# curl -h
# -H, --header LINE   Pass custom header LINE to server (H)
# -X, --request COMMAND  Specify request command to use
# -O, --remote-name   Write output to a file named as the remote file
# -r, --range RANGE   Retrieve only the bytes within RANGE

from os import system

# 方法一:
import requests
url = "http://www.qlcoder.com/download/hugefile"
headers = {'Range': 'bytes = 12345678901-12345678999'}
r = requests.get(url, headers=headers)
print r.text

# 方法二:
system('curl -X "GET" "http://www.qlcoder.com/download/hugefile" -H "Range: bytes=12345678901-"')
print
system('curl -X "GET" "http://www.qlcoder.com/download/hugefile" -H "Range: bytes=12345678901-12345678999"')

# 下面这行会输出文件
# system('curl -r 12345678901-12345678999 "http://www.qlcoder.com/download/hugefile" -O')
