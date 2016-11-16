#!/usr/bin/python
# coding: utf-8

# 一般而言，对于pc端，我们会在每个用户的cookie中种入一个uuid。 由于uuid是纯随机的16进制， 最简单的方式，就可以根据uuid的第一位，将所有用户分为16份。如果总共有160w用户，那么每份流量下就有10w用户。这样，就可以同时测试16种方案，最终统计这16份流量下的核心数据，便可以从中选出最优的方案了。
# 对于移动端，情况也是类似，不过移动端我们往往不需要为每个用户生成一个uuid，直接根据用户的手机设备号分组即可。
# 对于这道题考什么，qlcoder官方审题小组非常之纠结，于是决定根据用户的cookie中的uuid的第1位分成16个问题... 好啦，这里有一个页面,您的问题就在里面。

# 方法一:
# 直接修改 cookie, 用 Chrome 插件

# 方法二:
# Console: document.cookie="uuid=c"

# 问题
# 字符串"qlcoder"的md5值是多少?

import hashlib
print hashlib.md5('qlcoder').hexdigest()

