<?php
/*
请把它转成json格式,本题的答案是该json字符串
坑, 没有 root 根节点
 */
/*
<?xml version="1.0" encoding="UTF-8" ?>
    <name>Sayalic</name>
    <age>25</age>
    <girlfriend>null</girlfriend>
    <gayfriend>
        <age>24.5</age>
        <name>dploop</name>
        <FavoriteFruits>pear</FavoriteFruits>
        <FavoriteFruits>lemon</FavoriteFruits>
    </gayfriend>
    <FavoriteFruits>orange</FavoriteFruits>
    <FavoriteFruits>banana</FavoriteFruits>
    <FavoriteFruits>apple</FavoriteFruits>
 */
/**
{
  "name": "Sayalic",
  "age": "25",
  "girlfriend": "null",
  "gayfriend": {
    "age": "24.5",
    "name": "dploop",
    "FavoriteFruits": [
      "pear",
      "lemon"
    ]
  },
  "FavoriteFruits": [
    "orange",
    "banana",
    "apple"
  ]
}
 */
$xml = <<<jrp
<?xml version="1.0" encoding="utf-8"?>
<xml>
  <name>Sayalic</name>
  <age>25</age>
  <girlfriend>null</girlfriend>
  <gayfriend>
    <age>24.5</age>
    <name>dploop</name>
    <FavoriteFruits>pear</FavoriteFruits>
    <FavoriteFruits>lemon</FavoriteFruits>
  </gayfriend>
  <FavoriteFruits>orange</FavoriteFruits>
  <FavoriteFruits>banana</FavoriteFruits>
  <FavoriteFruits>apple</FavoriteFruits>
</xml>
jrp;
$a = simplexml_load_string("$xml");
echo json_encode($a);
?>

