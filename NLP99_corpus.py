from jpype import *
from pyhanlp import *
from collections import Counter
import os
import re
import pprint

def count_corpus(train_path:str,test_path:str):
    train_counter,train_freq,train_chars=count_word_freq(train_path)
    test_counter,test_freq,test_chars=count_word_freq(test_path)
    test_oov=sum(test_counter[w] for w in (test_counter.keys()-train_counter.keys()))
    return train_chars/int(1e4),len(train_counter)/int(1e4),train_freq/int(1e4),\
    train_chars/train_freq,test_chars/int(1e4),len(test_counter)/int(1e4), \
    test_freq/int(1e4),test_chars/test_freq,test_oov/test_freq*100

def count_word_freq(train_path):
    f=Counter()
    with open(train_path,encoding='utf-8') as src:
        for line in src:
            for word in re.compile('\\s+').split(line.strip()):
                f[word]+=1
    return f,sum(f.values()),sum(len(w)*f[w] for w in f.keys())

if __name__=='__main__':
    print('|语料库|字符数|词语种数|总词频|平均词长|字符数|词语种数|总词频|平均词长|OOV|')
    train=r'C:\Users\max21\Desktop\Python\NLP\icwb2-data\training'
    test=r'C:\Users\max21\Desktop\Python\NLP\icwb2-data\gold'
    for data in 'pku','msr','as','cityu':
        train_path=os.path.join(train,'{}_training.utf8'.format(data))
        test_path=os.path.join(test,\
            ('{}_testing_gold.utf8' if data=='as' else '{}_test_gold.utf8').\
            format(data))
        pprint.pprint('|%s|%.0f万|%.0f万|%.0f万|%.1f|%.0f万|%.0f万|%.0f万|%.1f|%.2f%%'%(
            (data,)+count_corpus(train_path,test_path)))


            




