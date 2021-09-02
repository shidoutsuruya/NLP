from jpype import *
from pyhanlp import *
import os
pinyin_list = JClass("com.hankcs.hanlp.dictionary.py.Pinyin")
print(HanLP.convertToTraditionalChinese('象. 之后 '))
print(HanLP.s2tw('可以将该值存'))

print(HanLP.convertToPinyinString("截至年，", " ", True))
print(HanLP.convertToPinyinString("截至年，", " ", False))
Pinyin = JClass("com.hankcs.hanlp.dictionary.py.Pinyin")

print('&'*20)
text = "重载不是重任！"
pinyin_list = HanLP.convertToPinyinList(text)
print(pinyin_list)
for pinyin in pinyin_list:
    print("%s," % pinyin.getPinyinWithoutTone(), end=" ")
    print("\n声调，", end=" ")
for pinyin in pinyin_list:
    print("%s," % pinyin.getTone(), end=" ")
print("\n声母，", end=" ")
for pinyin in pinyin_list:
    print("%s," % pinyin.getShengmu(), end=" ")
print("\n韵母，", end=" ")
for pinyin in pinyin_list:
    print("%s," % pinyin.getYunmu(), end=" ")
print("\n输入法头，", end=" ")
for pinyin in pinyin_list:
    print("%s," % pinyin.getHead(), end=" ")




