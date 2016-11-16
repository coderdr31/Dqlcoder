#!/usr/bin/python
# coding: utf-8

# 这里有一个文件夹，答案就在里面最大的text文档里面。
# 这个题就不提供运行环境了

from os import system

# 方法一:
system("find . -name "*txt" | xargs ls -li|sort -k 6|tail -n 1")

# xargs 将 find 的结果在 ls 执行一遍
# ls -l 第五列是大小, -i 插入一列 序号, 所以是第6列
# sort -k 参数, 以第6列为依据排序
# tail 从后面数, sort 升序排
# 升级版
# find . -name "*txt" | xargs ls -li|sort -k 6|tail -n 1| awk '{print $10}' | xargs cat

# 方法二:
# 将代码放到 下载的文件夹的外面同级目录下
import os

fileList = [path+'/'+file
    for path, _, files in os.walk("root/") for file in files]
targetFile = max(fileList, key=lambda x: os.path.getsize(x))
with open(targetFile) as answer:
    print(answer.read())
