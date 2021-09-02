from jpype import *
from pyhanlp import * 

word=['his','that','him']
Trie=JClass('com.hankcs.hanlp.algorithm.ahocorasick.trie.Trie')
trie=Trie()

for w in word:
    trie.addKeyword(w)
    
for emit in trie.parseText('usthat'):
    print('[%d:%d]=%s'%(emit.getStart(),emit.getEnd(),emit.getKeyword()))
#
string='北京市政协科技委员会'
HanLP.Config.ShowTermNature=False
segment=DoubleArrayTrieSegment()
print(segment.seg(string))

#input the dictionary
dict1=r'C:\Users\max21\AppData\Roaming\Python\Python37\site-packages\pyhanlp\static\data\dictionary\custom\机构名词典.txt'
segment=DoubleArrayTrieSegment(dict1)
print(segment.seg(string))

segment.enablePartOfSpeechTagging(True)
HanLP.Config.ShowTermNature=True
print(segment.seg(string))

for term in segment.seg(string):
    print('volcabulary:%s,nature:%s'%(term.word,term.nature))


