# -*- coding:utf-8 -*-
# Author：hankcs
# Date: 2018-07-04 15:13

def convert(src, dst):
    with open(src) as src, open(dst, 'w') as dst:
        for line in src:
            dst.write(line.replace('_', '/'))


convert('eacl14mszhang/dev.zhuxian.wordpos', 'dev.txt')
convert('eacl14mszhang/train.zhuxian.wordpos', 'train.txt')
convert('eacl14mszhang/test.zhuxian.wordpos', 'test.txt')
