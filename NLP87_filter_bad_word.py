from jpype import *
from pyhanlp import *
import os

def load_from_file(path):
    map=JClass('java.util.TreeMap')()
    with open(path,encoding='utf-8') as src:
        for word in src:
            word=word.strip()
            map[word]=word
    return JClass('com.hankcs.hanlp.collection.trie.DoubleArrayTrie')(map)

def load_from_words(*words):
    map=JClass('java.util.TreeMap')()
    for word in words:
        map[word]=word
    print(map)
    return JClass('com.hankcs.hanlp.collection.trie.DoubleArrayTrie')(map)

def remove_stopwords_termlist(termlist,trie):
    return [term.word for term in termlist if not trie.containsKey(term.word)]

def replace_stropwords_text(text,replacement,trie):
    searcher=trie.getLongestSearcher(JString(text),0)
    offset=0
    result=''
    while searcher.next():
        begin=searcher.begin
        end=begin+searcher.length
        if begin>offset:
            result+=text[offset:begin]
        result+=replacement
        offset=end
    if offset<len(text):
        result+=text[offset]
    return result

HanLP.Config.ShowTermNature=False
path=r'C:\Users\max21\Desktop\Python\NLP\data\dictionary\stopwords.txt'
trie=load_from_file(path)
text='停用傻瓜词相对而言就是没有必要的吧'
#put into tree
segment=DoubleArrayTrieSegment()
#handle word
termlist=segment.seg(text)
print('consequence:',termlist)
print('filt stropword:',remove_stopwords_termlist(termlist,trie))
trie=load_from_words('的','相对而言','吧')
print('transform:',replace_stropwords_text(text,'**',trie))





