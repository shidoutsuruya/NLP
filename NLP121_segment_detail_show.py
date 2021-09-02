from jpype import *
from pyhanlp import *
import os

NatureDictionaryMaker = SafeJClass('com.hankcs.hanlp.corpus.dictionary.NatureDictionaryMaker')
CorpusLoader = SafeJClass('com.hankcs.hanlp.corpus.document.CorpusLoader')
WordNet = JClass('com.hankcs.hanlp.seg.common.WordNet')
Vertex = JClass('com.hankcs.hanlp.seg.common.Vertex')
ViterbiSegment = JClass('com.hankcs.hanlp.seg.Viterbi.ViterbiSegment')
DijkstraSegment = JClass('com.hankcs.hanlp.seg.Dijkstra.DijkstraSegment')
CoreDictionary = LazyLoadingJClass('com.hankcs.hanlp.dictionary.CoreDictionary')
Nature = JClass('com.hankcs.hanlp.corpus.tag.Nature')
CWSEvaluator=JClass('com.hankcs.hanlp.seg.common.CWSEvaluator')


def train_bigram(corpus_path,model_path):
    sents=CorpusLoader.convert2SentenceList(corpus_path)
    for sent in sents:
        for word in sent:
            word.setLabel('n')
    maker=NatureDictionaryMaker()
    maker.compute(sents)
    maker.saveTxtTo(model_path)
    print('Sucessful save')

def load_bigram(model_path):
    #input path
    HanLP.Config.CoreDictionaryPath = model_path + ".txt"  # unigram
    HanLP.Config.BiGramDictionaryPath = model_path + ".ngram.txt"  # bigram
    return DijkstraSegment().enableAllNamedEntityRecognize(False).enableCustomDictionary(
        False) 

#create dictionary
corpus_path=r'C:\Users\max21\Desktop\Python\NLP\icwb2-data\training\msr_training.utf8'
model_path=r'C:\Users\max21\Desktop\Python\NLP\model\model'
train_bigram(corpus_path,model_path)

seg=load_bigram(model_path)
assert CoreDictionary.contains('机场')
text='北京大兴机场工程'
HanLP.Config.enableDebug()
print(seg.seg(text))




