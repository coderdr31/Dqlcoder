#!/usr/bin/python
# coding: utf-8

# 每一个网站都会根据访客日志统计访客数据，比如UV（Unique Visitor，即访问用户）。
# UV能够回答一个关键的市场营销问题：“到底有多少人（潜在客户）看到了你发布的信息（即网站）”。
# 这道题的任务是根据给出的某购物网站访问日志，统计当天该网站UV。
# 日志文件的每一行代表一次访问行为，每行分别包含三项，以空格分隔，格式为：
# 用户访问的时间 用户的id 用户的行为

# 请问8月24号当天，该网站有多少个用户（相同用户id算一个用户）访问？
''' 部分数据如下
2015-08-24_00:00:00 55311 buy
2015-08-24_00:00:01 73069 add2cart
2015-08-24_00:00:02 62843 add2cart
2015-08-24_00:00:03 14187 search
2015-08-24_00:00:04 77895 pay
2015-08-24_00:00:05 81708 pay
'''
import os
from os import system

filename = '5.uv.txt'
fileurl = 'http://www.qlcoder.com//download/uv.txt'
# 下载文件
if not os.path.isfile(filename):
    print('下载数据文件……')
    import requests
    r = requests.get(fileurl)
    # 这里的 r.content 是 str 类型的
    # 要写到文件中再一行行的读出来
    with open(filename, 'wb') as f:
        f.write(r.content)

f = open(filename)
# 推荐:
print(len({i.split(' ')[1] for i in open(filename)}))

# 计算 方法一
iddic = {}
cont = 0
for line in f.readlines():
    temp = line.split(' ')
    id = temp[1]
    if id not in iddic:
        iddic[id] = True
        cont += 1
print('访客数{}'.format(cont))

# 方法二: 集合的特性
num = set()
with open(filename) as f:
    s = f.readlines()
    i = 0
    while i != len(s):
        x = s[i].split(' ')
        num.add(x[1])
        i = i + 1
print(len(num))

# 方法三:
# 导入到excel, 去重
# =COUNT(1/FREQUENCY(B1:B90000,B1:B90000))

# 方法四:
cmd = "grep 2015-08-24 " + filename + " | awk '{print $2}' | sort | uniq -c | wc -l"
system(cmd)

