import re
import os
from jpype import *
from pyhanlp import *
import time
time_start=time.time()

def to_region(segmentation:str)->list:
    region=[]
    start=0
    for word in re.compile('\\s+').split(segmentation.strip()):
        end=start+len(word)
        region.append((start,end))
        start=end
    return region

a='hello world is my'
print(to_region(a))

def prf(gold:str,pred:str):
    #gold:standard answer
    #ptr:need to be predicted
    A_size,B_size,A_cap_B_size=0,0,0
    with open(gold) as gd,open(pred) as pd:
        for g,p in zip(gd,pd):
            A,B=set(to_region(g)),set(to_region(p))
            A_size+=len(A)
            B_size+=len(B)
            A_cap_B_size+=len(A&B)
    p,r=A_cap_B_size/B_size,A_cap_B_size/A_size
    return p,r,2*p*r/(p+r)
path=r'C:\Users\max21\Desktop\Python\NLP\icwb2-data'
msr_dict=os.path.join(path,'gold','as_training_words.utf8')
msr_test=os.path.join(path,'testing','msr_test.utf8')
msr_output=os.path.join(path,'testing','msr_output.txt')
msr_gold=os.path.join(path,'gold','msr_test_gold.utf8')

DoubleArrayTrieSegment=JClass('com.hankcs.hanlp.seg.Other.DoubleArrayTrieSegment')
segment=DoubleArrayTrieSegment([msr_dict]).enablePartOfSpeechTagging(True)
with open(msr_gold,encoding='utf-8') as test,open(msr_output,'w',encoding='utf-8') as output:
    for line in test:
        output.write(' '.join(term.word for term in segment.seg(re.sub('\\s+','',line))))
        output.write('\n')

time_end=time.time()
print('time cost',time_end-time_start,'s')
print('P:%.2f,R:%.2f,F1:%.2f OOV-R:%.2f,IV-R:%.2f'%prf(msr_gold,msr_output,segment.trie))
