<?php
# 很多时候我们会需要持久化用户的数据,存储用户的数据有非常多的方式，
# 比如文件系统，数据库（mysql等）,缓存（memcache，redis等）。

# 请提供一个url（即在答案框内输入你制作的网页的url，网页字符编码请用UTF-8），
# 这个url能接受1个名为registerusername的参数，代表一个用户注册了该网站。

# 如果该用户名还未被使用，那么返回"register success"。
# 否则返回 "already used"。
# 用户访问url的形式举例:

# http://121.201.63.168/train/register?registerusername=shinian
# (第一次访问，由于shinian没注册，返回 "register success")

# http://121.201.63.168/train/register?registerusername=shinian
# (第二次访问，由于shinian已经注册了，返回 "already used")

# http://121.201.63.168/train/register?registerusername=jiaye
# (第三次访问，由于jiaye没注册，返回 "register success")

# 这里你提交的答案不需要带参数,只需提交: http://121.201.63.168/train/register 即可

# 自己测试的 URL:
# http://localhost:9999/59.我要建站-3_操作数据库.php?registerusername=jrp

# 服务器执行
# php -S 115.28.247.19:9999
# 服务器 URL
# http://115.28.247.19:9999/jrp.php?registerusername=shinian

# 方法一: 一行代码
# echo file_exists(__DIR__.'/'.$_GET['registerusername']) ? 'already used' : 'register success'; fopen(__DIR__.'/'.$_GET['registerusername'] , 'w');

# 方法二:
$n = isset($_GET['registerusername']) ? $_GET['registerusername'] : '';
if(!$n) {
    exit('empty');
}

$db = file_get_contents('/tmp/qlcoder_db');
$db = json_decode($db, true);

if(isset($db[$n])) {
    exit('already used');
} else {
    $db[$n] = 1;
    $content = json_encode($db);
    file_put_contents('/tmp/qlcoder_db', $content);
    exit('register success');
}

?>
