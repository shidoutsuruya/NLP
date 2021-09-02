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

segment=ViterbiSegment()
sentence='社会摇摆简称社会摇'
#NOT USE DICTIONARY
segment.enableCustomDictionary(False)
print('not use dictionary:',segment.seg(sentence))
#USE NORMAL DICTIONARY
CustomDictionary.insert('社会摇','nz 100')
segment.enableCustomDictionary(True)
print('normal dictionary:',segment.seg(sentence))
#USE FORCED DICTIONARY
segment.enableCustomDictionaryForcing(True)
print('forced dictionary:',segment.seg(sentence))


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
    return ViterbiSegment().enableAllNamedEntityRecognize(False).enableCustomDictionary(
        False) 

#create dictionary
corpus_path=r'C:\Users\max21\Desktop\Python\NLP\icwb2-data\training\msr_training.utf8'
model_path=r'C:\Users\max21\Desktop\Python\NLP\model\model'
train_bigram(corpus_path,model_path)
seg=load_bigram(model_path)

#test accuracy
msr_test=r'C:\Users\max21\Desktop\Python\NLP\icwb2-data\testing\msr_test.utf8'
msr_output=r'C:\Users\max21\Desktop\Python\NLP\icwb2-data\testing\msr_output.utf8'
msr_gold=r'C:\Users\max21\Desktop\Python\NLP\icwb2-data\gold\msr_test_gold.utf8'
msr_dict=r'C:\Users\max21\Desktop\Python\NLP\icwb2-data\gold\msr_training_words.utf8'                                               

result=CWSEvaluator.evaluate(seg,msr_test,msr_output,msr_gold,msr_dict)
print(result)



