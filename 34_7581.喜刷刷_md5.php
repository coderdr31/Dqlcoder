<?php

// 程序运行时间: 307 min

//这里有一个最帅coder评选排行榜… http://www.qlcoder.com/train/handsomerank
//用户可以上传他认为最帅的coder的名字及其头像，并为他点赞…
//被点赞数超过1000的coder，通过此题…
//一般点赞这种行为会设计一个验证码…来区别您是普通人还是机器…

//我们网站是coder专享的…验证码当然会难一点啦~ 这里的验证码是
//一个自然数x…他能使 md5(当天日期+你的用户名+当前的票数+x)的前6位都是0…
//举例: 假如2015年12月4号食年已经拿到了1014票,当你想投第1015票的时候,你的验证码可以是12011618,
//因为 "20151204shinian101412011618"的md5值是"0000003A19CF73CF3E9799219A9FFF4F",这个md5前6位都是0…
//当你的票数超过1000，再次投票即可看见答案

// 用的是单线程, 可以考虑多线程加速

// 可以先测验一下时区
//echo date_default_timezone_get();
date_default_timezone_set("Asia/Shanghai");

$f = fopen("data", "w");
$stime = microtime(true);

$str = date('Ymd').'drcoder';
for($i = 1; $i <= 1000; $i++)
{
    $stri = $str.$i;
    $code = 0;
    while(true)
    {
        $md5 = md5($stri.$code);
        if (substr($md5, 0, 6) === '000000') {
            file_get_contents("http://www.qlcoder.com/train/handsomerank?_token=token&user=drcoder&checkcode=".$code);
            //echo "已经刷了".$i."票";
            fwrite($f, "已经刷到".$i."票"."\n");
            break;
        }
        $code++;
    }
}
$etime = microtime(true);
$total = $etime - $stime;
fwrite($f, $total);
?>
