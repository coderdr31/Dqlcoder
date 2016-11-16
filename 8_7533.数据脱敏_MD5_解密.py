# !/usr/bin/python
# encoding: utf-8

# 由于一次攻击事件,黑客拿到了shinian的32位经过MD5哈希后的密码7E38890B870934B126F66857ED6B57B9, 而shinian又是一个很喜欢用8位生日数字作为密码的人……糟糕，好像暴露了什么呢！这题的答案就是shinian的密码明文。
import hashlib
ans = "7E38890B870934B126F66857ED6B57B9"
for i in range(19200101, 20101231):
    s = "{0}".format(i)
    # print type(s)  # str
    m = hashlib.md5(s.encode('utf-8'))
    # print m  # <md5 HASH object @ 0x7fadb15d5800>
    # print m.hexdigest()  # 978bc4d5f34a8e47fc10605b072ace9e
    if m.hexdigest().upper() == ans:
        print(i)
        break
