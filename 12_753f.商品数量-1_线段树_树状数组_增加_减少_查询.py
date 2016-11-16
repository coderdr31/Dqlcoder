#!/usr/bin/python
# coding: utf-8

# 可以用树状数组来优化, 见 hdu1166

# 接下来包含一个含有多行的文本文件，文件的每行代表上架，下架，查询三种行为的一种，本题默认查询对象是衣服。
#
# 所有买家查询结果的总和就是本题的答案。
#
# 举例: 一个拥有6行的文件。
#
# up 3 11 （有一个商家上架了3件11rmb的衣服。）
# query 11 25 (有一个买家查询11rmb-25rmb的衣服的数量。这里的查询结果是:3件)
# up 5 25 （有一个商家上架了5件25rmb的衣服。）
# query 11 25 (有一个买家查询11rmb-25rmb的衣服的数量。这里的查询结果是:8件)
# down 3 25 （有一个商家下架了3件25rmb的衣服。）
# query 20 25 （有一个买家查询20rmb-25rmb的衣服的数量。这里的查询结果是:2件）
#
# 所以在这个例子里所有买家查询结果的总和为13（3+8+2=13）。

import os #包含普遍的操作系统功能，跨平台
from os import system

fileurl = "http://www.qlcoder.com/download/144043123647536.txt"
filename = "12_753f.dat"

if not os.path.isfile(filename):
    print "downloading ..."
    import requests
    r = requests.get(fileurl)
    with open(filename, "wb") as f:
        f.write(r.content)

f = open(filename)
# 方法一: 比较慢
ans = 0
h = []
for i in range(0, 1000):
    h.append(0)

for line in f.readlines():
    line = line.strip('\n')
    args = line.split(' ')
    if args[0] == 'up':
        h[int(args[2])] += int(args[1])
    elif args[0] == 'down':
        h[int(args[2])] -= int(args[1])
    elif args[0] == 'query':
        for i in range(int(args[1]), int(args[2]) + 1):
            ans += h[i]

print ans

# 方法二:  awk
system("cat 12_753f.dat | awk '{if($1 == \"up\"){a[$3] += $2} if($1 == \"down\"){a[$3] -= $2} if($1 == \"query\"){s = 0; for(i in a){if(int(i) >= int($2) && int(i) <= int($3)) s += a[i];} print s;}}' | awk '{s += $1} END {print s}'")

# 方法三:
good = {}
sum = 0
with open(filename) as f:
    for line in f.readlines():
        action, num1, num2 = line.split("\n")[0].split(" ")
        if action == "up":
            good[num2] = good.get(num2, 0) + int(num1)
        elif action == "down":
            good[num2] = good.get(num2, 0) - int(num1)
        elif action == "query":
            for key, value in good.items():
                if int(key) >= int(num1) and int(key) <= int(num2):
                    sum = sum + value
print sum
