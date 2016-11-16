<?php

// 开启 server 和 数据库
// 去官网 下载 medoo.php
// 需要先执行 ./59.test.sql 文件,来建立数据库

require("medoo.php");
// $db = new medoo();  // 创建medoo 数据库对象，需要在medoo.php文件内配置连接数据库参数
$db = new medoo(array(  // 这样创建不用修改 medoo.php
    'database_type' => 'mysql', //连接类型：mysql、mssql、sybase, mariadb属于 mysql
    'database_name' => 'jrp', //数据库名
    'server' => 'localhost', //数据库地址
    'username' => 'root', //数据库账号
    'password' => 'root', //数据库密码
));
$name = $_GET['registerusername'];
//查询符合条件name=$name的记录 //返回一个符合条件的数组
$rz = $db->select("dr",["name"],[
    "name"=>$name
]);
//数组长度大于0，说明存在这个记录
if( count($rz)>0 ){
    echo "already used";
}else{
    //不存在记录，插入数据库，然后返回注册成功
    $falg = $db->insert("dr",[
        "name"=>$name
    ]);
    echo "register success";
}
?>
