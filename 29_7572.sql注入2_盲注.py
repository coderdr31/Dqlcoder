#!/usr/bin/python
# coding: utf-8

# 测试页面: http://www.qlcoder.com/train/admin2
# 教程页面: http://www.qlcoder.com/q/7638

# 盲注(Blind SQL Injection)是一种SQL注入。和一般SQL注入的区别在于盲注没有办法从页面上直接拿到想要的内容，
# 但是可以通过页面返回的内容来得知SQL语句执行的结果，再通过该结果来间接获得目标内容。
# 比如SQL1的那个登录入口，有三种结果：
# 登录成功
# 登录失败
# SQL语句错误

# 这个页面本身不会直接展示任何数据库的内容，但是通过登录是否成功能知道SQL语句的结果如何。

# 接着 9. sql注入1

# 下一步，我们输入用户名shinian' and substr(password,1,1) = 'a'#，这样SQL变为：
# SELECT * FROM USERS WHERE username = 'shinian' and substr(password,1,1) = 'a'
# substr(x,y,z)是取x的第y位长度为z的字串。substr(password,1,1)表示密码的第一位。
# 也就是说，如果我们登录成功，那么说明密码的第一位是a。
# 使用这样的方法一位一位地去试探，就可以得到shinian的登录密码，但你会发现这个密码是加密过的。
# 那么你需要碰撞，也就是说加密是函数f(x)，shinian加密后的密码是v，那么你需要找到一个字符串y，使得f(y)=v。
# 这个办法可行，但是非常难。还有另外一种方法：

# 构造一个SQL（自己思考如何构造）使得：
# 登录成功 - X库.Y表.Z字段的第N行的第P位等于字符C
# 登录失败 - X库.Y表.Z字段的第N行的第P位不等于字符C

# 这样有个问题，如果SQL1的那个登录入口使用的数据库和SQL2使用的数据库不一样怎么办呢？
# 经过一番折腾，你最终会发现SQL2的提交接口并不能注入。所以过来人给点提示——如果那样还注入个毛啊，
# 所以SQL1里面取出来的数据必然是SQL2能用的。
# 如此这般，可以把整个库都全部读出来，当然，任务的答案一般会放在数据库里面。

# 这里有个问题，数据里面有很多东西，一位一位地去读，把整个库全部读出来，不太现实。
# 那么我们需要先获取整个数据库的(库，表，字段)信息，根据库名表名字段名猜测答案在哪个表里面，
# 按图索骥，直奔主题。那么，如何获得一个数据库实例里面所有的(库，表，字段)列表呢？

# 这个问题涉及到网站使用的数据库版本(MySQL, Oracle, MSSQL)，但是这种个人网站，基本都是使用MySQL，
# 所以我们就先假设该网站使用的是MySQL。

# 而MySQL每个实例中都有个库叫做information_schema，这个库里面就存着里面你想要的(库，表，字段)列表。
# 我使用SqlFiddle把前几个例子做了一个SQL在线调试环境，你们可以去试试：
# =>调试环境传送门<= http://sqlfiddle.com/#!9/28430f/11


# SqlFiddle时好时坏，这里备份一下我的测试用例
# SCHEMA
'''
CREATE TABLE USERS
    (`id` int, `username` varchar(10), `password` varchar(10))
;

CREATE TABLE TASKS
    (`id` int, `name` varchar(10), `answer` varchar(10))
;

INSERT INTO USERS
    (`id`, `username`, `password`)
VALUES
    (1, 'shinian', 'badboy'),
    (2, 'Sayalic', 'goodboy')
;

INSERT INTO TASKS
    (`id`, `name`, `answer`)
VALUES
    (1, '码之初', '3500'),
    (2, 'SQL2', 'magickey')
;
'''
# SQL
'''
# 原始SQL语句 SELECT * FROM USERS WHERE username = '${username}' and password = '${password}';

# 正常登录，密码不知道，登录失败
SELECT * FROM USERS WHERE username = 'shinian' and password = 'hardtoget';

# 基本注入，用户名输入shinian'#，密码留空，登录成功
SELECT * FROM USERS WHERE username = 'shinian'# and password = '';

# 输入shinian' and substr(password,1,1) = 'a'#，检测密码第一位是否为a
# 返回为空，登录失败，说明密码第一位不为a
SELECT * FROM USERS WHERE username = 'shinian' and substr(password,1,1) = 'a'# and password = '';
# 同理，检测密码第一位是否为b
# 返回不为空，登录成功，说明密码第一位为b
SELECT * FROM USERS WHERE username = 'shinian' and substr(password,1,1) = 'b'# and password = '';

# 剩下的任务：
# 1. 尝试拿到加密的密码，但是你会发现碰撞很难
# 2. 直接从数据库拿到SQL2的答案，就在某个库里面，可是怎么取出来呢？
'''
