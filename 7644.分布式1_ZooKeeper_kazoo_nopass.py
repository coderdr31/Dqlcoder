#!/usr/bin/python
# coding: utf-8

# okok，这里是zookeeper的官网，里面有zookeeper的教程，目前qlcoder在服务器121.201.8.217上部署了zookeeper，
# 版本号：3.4.8，对外的端口是2181。当你用zookeeper的client连上之后，
# 查看/qlcoder/zookeeper节点，就能看到本题的答案了。

# http://www.qlcoder.com/task/7644
# pip install kazoo

from kazoo.client import KazooClient

zk = KazooClient(hosts='121.201.8.217:2181')
zk.start()
data, stat = zk.get("/qlcoder/zookeeper")
print("Version: %s, data: %s" % (stat.version, data.decode("utf-8")))
