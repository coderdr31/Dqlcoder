<?php
header("Content-type: text/html; charset=utf-8");
# 请提供一个URL（即在答案框内输入你制作的网页的URL，网页字符编码请用UTF-8），这个URL能接收两个参数a和b，返回a*b的值。
# 比如当a=4,b=5的时候，你应该返回20。

# 开一个 php 内置 server, 测试一下 ?a=4&b=5
# vps 上运行这句话
# php -S 115.28.247.19:9999
$a = (int)$_GET['a'];
$b = (int)$_GET['b'];

# 第二种方法:
//$a = $_GET['a'];
//$b = $_GET['b'];
//$a = intval($a);
//$b = intval($b);

echo $a*$b;
?>
