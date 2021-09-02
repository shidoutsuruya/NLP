from jpype import * 
from pyhanlp import *
import time
import numpy as np
import matplotlib.pyplot as plt
def load_dictionary():
    IOUtil=JClass('com.hankcs.hanlp.corpus.io.IOUtil')
    path=HanLP.Config.CoreDictionaryPath.replace('.txt','.mini.txt')
    dic=IOUtil.loadDictionary([path])
    return set(dic.keySet())

dic=load_dictionary()
string='项目的研究，当下雨天路面积水，结婚的和尚未结婚'
def fully_segment(text,dic):
    word_list=[]
    for i in range(len(text)):
        for j in range(i+1,len(text)+1):
            word=text[i:j]
            if word in dic:
                word_list.append(word)
    return word_list

print('fully segment:')
print(fully_segment(string,dic))

def forward_segment(text,tic):
    word_list=[]
    i=0
    while i <len(text):
        longest_word=text[i]
        for j in range(i+1,len(text)+1):
            word=text[i:j]
            if word in dic:
                if len(word)>len(longest_word):
                    longest_word=word
        word_list.append(longest_word)
        i+=len(longest_word)
    return word_list
print('forward segment:')
print(forward_segment(string,dic))

def backward_segment(text,dic):
    word_list=[]
    i=len(text)-1
    while i>=0:
        longest_word=text[i]
        for j in range(0,i):
            word=text[j:i+1]
            if word in dic:
                if len(word)>len(longest_word):
                    longest_word=word
        word_list.insert(0,longest_word)
        i-=len(longest_word)
    return word_list

print('backward segment:')
print(backward_segment(string,dic))


def count_single_char(word_list:list):
    return sum(1 for word in word_list if len(word)==1)

def bidirectional_segment(text,dic):
    f=forward_segment(text,dic)
    b=backward_segment(text,dic)
    if len(f)<len(b):
        return f
    elif len(f)>len(b):
        return b
    else:
        if count_single_char(f)<count_single_char(b):
            return f
        else:
            return b
print('bidirectional segment:')
print(bidirectional_segment(string,dic))

def evaluate_speed(segment,text,dic):
    start_time=time.time()
    for i in range(pressure):
        segment(text,dic)
    elapsed_time=time.time()-start_time
    value=round(len(text)*pressure/1e4/elapsed_time,2)
    print('%.2f/s'%(value))
    return value

if __name__=='__main__':
    pressure=int(1e4)
    dic=load_dictionary()

lst=[    evaluate_speed(forward_segment,string,dic),
    evaluate_speed(backward_segment,string,dic),
    evaluate_speed(bidirectional_segment,string,dic)   ]

label=['forward','backward','bidirection']
wid=0.25
fig,ax=plt.subplots()

x=np.arange(len(label))
rest=ax.bar(x,lst,wid,label='speed',color='orange')
ax.set_ylabel('SPEED')
ax.set_title('speed of segment')
ax.set_xticks(x)
ax.set_xticklabels(label)
ax.legend()

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(rest)
fig.tight_layout()
plt.show()
