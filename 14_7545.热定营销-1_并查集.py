#!/usr/bin/python
# coding: utf-8

# 现在的问题来了，这是100个微信用户的关系列表。为了方便表达，把名字变成一个整数，
# 这100个用户的名字分别为1-100。每行有两个名字，代表这两人互为微信好友。

# 你需要使一个广告让这100个微信用户都看到，请问初始至少将这条广告传播给几个人？
# 假设这条广告编写得很精美，因此用户们看到一定会转发在他的朋友圈让他的朋友看到的。
# http://www.qlcoder.com/task/7545
import os
import networkx as nx

filename = '14.data'
fileurl = 'http://qlcoder.com/download/144047638844506.txt'
if not os.path.isfile(filename):
    print('下载数据文件……')
    import requests
    r = requests.get(fileurl)
    with open(filename, 'wb') as f:
        f.write(r.content)

# 推荐: networkx
f = open(filename)
g = nx.Graph()
for line in f.readlines():
    temp = line.split(' ')
    a = int(temp[0]) - 1
    b = int(temp[1]) - 1
    g.add_edge(a, b)
print nx.number_connected_components(g)  # 判断有几个连通子图
f.close()

# 方法一:
f = open(filename)
usernum = 100
users = [[i] for i in range(usernum)]

for line in f.readlines():
    temp = line.split(' ')
    a = int(temp[0]) - 1
    b = int(temp[1]) - 1
    if users[b] != users[a]:
        for k in users[b]:
            users[a].append(k)
            users[k] = users[a]

count = 0
for i in range(usernum):
    if users[i] is not None and users[users[i][0]] is not None:
        print('圈子{}，长度{}'.format(users[i], len(users[i])))
        count += 1
        users[users[i][0]] = None

print('共有圈子{}个'.format(count))
