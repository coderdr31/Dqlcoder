#!/usr/bin/python
# coding: utf-8
# 压缩算法在IT领域运用面非常之广。
# 文件压缩（zip，rar，tar)
# 图片压缩（jpg，png）
# 音频（mp3）
# 动画的帧内压缩和帧间压缩
# 最最最简单的字符串压缩方式就是游程编码
#
# 举例:
#
# 压缩前的字符串是: dfffffeeeeettttrrrrttttt （长度:24）
# 压缩后是: d1f5e5t4r4t5 (长度:12)为了方便大家理解避免歧义,本题中如果连续出现30个a,会被压缩成9a9a9a3a
# 将连续出现的字符统计出来表示成字符+数字的形式。
# 压缩了50%。
#
# 但是实际情况，往往有很多字符串，没有连续几个字符在一起的情况。比如banana。
# 压缩前: bananabananabanana(长度:18)
# 压缩后: b1a1n1a1n1a1b1a1n1a1n1a1b1a1n1a1n1a1(长度:36)
# 非常的sad..反而越压越长了…
# 肿么办,Burrows–Wheeler transform是一个优秀的重排序方案。请仔细看wiki中的例子以及"^|"的意义。
# 经过bwt之后
# ^bananabananabanana| 就变成了 |nnnnbbbnn^aaaaaaaaa (其中^代表原字符串头，|代表原字符串尾)
# |nnnnbbbnn^aaaaaaaaa 就可以按照游程编码压缩成为 |1n4b3n2^1a9（长度:12）
# 当然，我们也可以根据相应的|1n4b3n2^1a9 还原得到原来的字符串。
# 接下来有一段歌词，摘自小黄人banana之歌:BABABABANANABABABABABANANABABABABABANANABANANANAAHH
# 这题的答案是 这段歌词 bwt算法外加游程编码后的压缩结果。


def wheelerTransform(data):
    data = "^" + data + "|"
    length = len(data)
    rotations = []
    for i in range(length, 0, -1):
        rotations.append(data[i:length] + data[0:i])
    rotations.sort()
    result = ""
    for r in rotations:
        result += r[length - 1]
    return result

def compress(data):
    result = ""
    count = 1
    cur = data[0]
    for d in data[1:]:
        if(d != cur):
            result += cur + str(count)
            count = 1
            cur = d
        else:
            count += 1
    return result + cur + str(count)

if __name__=='__main__':
    wt = wheelerTransform("BABABABANANABABABABABANANABABABABABANANABANANANAAHH")
    print wt
    print compress(wt)  # N3B11N1A1N5B4A2^1A13H1A9|1H1
