#!/bin/bash
# 为了使大家对openssl能有一个更加深入的了解， 下面有一个使用openssl blowfish加密方式加密的文件， 
# 使用openssl解密之后就能看到答案了哦。 blowfish的解密密码是[qlcoder]。
curl http://www.qlcoder.com/download/blowfish.data | openssl blowfish -d -pass pass:qlcoder
