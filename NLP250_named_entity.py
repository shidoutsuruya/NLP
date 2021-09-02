from pyhanlp import *
import os
CharType = JClass('com.hankcs.hanlp.dictionary.other.CharType')
ViterbiSegment=SafeJClass('com.hankcs.hanlp.seg.Viterbi.ViterbiSegment')

segment=ViterbiSegment()
text='牛奶一二四块2000g，现在打八五折的11~3牛奶'
print(segment.seg(text))
CharType.set('~',CharType.CT_NUM)
print(segment.seg(text))

