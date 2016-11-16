#!/usr/bin/python
# coding: utf-8
# 和 14 比起来只是 数据量更大
# 有些人没在文件中, 是孤立的...

import os
import networkx as nx
import time

filename = '15.data'
fileurl = 'http://121.201.63.168/download/144341511030664.txt'
if not os.path.isfile(filename):
    print('下载数据文件……')
    import requests
    r = requests.get(fileurl)
    with open(filename, 'wb') as f:
        f.write(r.content)

start_time = time.time()
cnt = set()
f = open(filename)
g = nx.Graph()
for line in f.readlines():
    temp = line.split(' ')
    a = int(temp[0]) - 1
    b = int(temp[1]) - 1
    cnt.add(a)
    cnt.add(b)
    g.add_edge(a, b)
print nx.number_connected_components(g) + 100000 - len(cnt)  # 判断有几个连通子图
end_time = time.time()
print("total time: {}".format(end_time - start_time))
f.close()
