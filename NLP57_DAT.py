from jpype import *
from pyhanlp import *

def load_dictionary():
    IOUtil=JClass('com.hankcs.hanlp.corpus.io.IOUtil')
    path=HanLP.Config.CoreDictionaryPath.replace('.txt','.mini.txt')
    dic=IOUtil.loadDictionary([path])
    return set(dic.keySet())

dic=load_dictionary()

class DoubleArrayTrie(object):
    def __init__(self,dic:dict)->None:
        m=JClass('java.util.TreeMap')()
        for k,v in dic.items():
            m[k]=v
        dat=JClass('com.hankcs.hanlp.collection.trie.DoubleArrayTrie')(m)

        self.base=dat.base
        self.check=dat.check
        self.value=dat.v

    def char_hash(c)->int:
        return JClass('java.lang.Character')(c).hashCode()
    def transition(self,c,b)->int:
        p=self.base[b]+self.char_hash(c)+1
        if self.base[b]==self.check[p]:
            return p
        else:
            return -1

    def __getitem__(self,key:str):
        b=0
        for i in range(0,len(key)):
            p=self.transition(key[i],b)
            if p is not -1:
                b=p
            else:
                return None

        p=self.base[b]
        n=self.base[p]
        if p==self.check[p] and n<0:
            index=-n-1
            return self.value[index]
        return None

if __name__=='__main__':
    dic={'自然':'nature','自然の家':'nature family'}
    dat=DoubleArrayTrie(dic)

