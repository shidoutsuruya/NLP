from jpype import *
from pyhanlp import *

CorpusLoader = SafeJClass('com.hankcs.hanlp.corpus.document.CorpusLoader')
NatureDictionaryMaker=SafeJClass('com.hankcs.hanlp.corpus.dictionary.NatureDictionaryMaker')
corpus_path=r'C:\Users\max21\Desktop\Python\NLP\corpus.txt'
model_path=r'C:\Users\max21\Desktop\Python\NLP\model'

def train_bigram(corpus_path,model_path):
    sents=CorpusLoader.convert2SentenceList(corpus_path)
    for sent in sents:
        for word in sent:
            word.setLabel('n')

    maker=NatureDictionaryMaker()
    maker.compute(sents)
    maker.saveTxtTo(model_path)
    print('Sucessful save')

train_bigram(corpus_path,model_path)
def load_bigram(model_path):
    #input path
    HanLP.Config.CoreDictionaryPath=model_path+'.txt'
    HanLP.Config.BiGramDictionaryPath=model_path+'.ngram.txt'   
    CoreDictionary=SafeJClass('com.hankcs.hanlp.dictionary.CoreDictionary')
    CoreBiGramTableDictionary\
        =SafeJClass('com.hankcs.hanlp.dictionary.CoreBiGramTableDictionary')
    print(CoreDictionary.getTermFrequency('们'))
    print(CoreBiGramTableDictionary.getBiFrequency('国家','主席' ))

load_bigram(model_path)




