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

def generate_wordnet(sent, trie):
    searcher = trie.getSearcher(JString(sent), 0)
    wordnet = WordNet(sent)
    while searcher.next():
        wordnet.add(searcher.begin + 1,
                    Vertex(sent[searcher.begin:searcher.begin + searcher.length], searcher.value, searcher.index))
    vertexes = wordnet.getVertexes()
    i = 0
    while i < len(vertexes):
        if len(vertexes[i]) == 0:  
            j = i + 1
            for j in range(i + 1, len(vertexes) - 1):  
                if len(vertexes[j]):
                    break
            wordnet.add(i, Vertex.newPunctuationInstance(sent[i - 1: j - 1]))  
            i = j
        else:
            i += len(vertexes[i][-1].realWord)

    return wordnet

def viterbi(wordnet):
    nodes=wordnet.getVertexes()
    for i in range(0,len(nodes)-1):
        for node in nodes[i]:
            for to in nodes[i+len(node.realWord)]:
                to.updateFrom(node)

    path=[]
    f=nodes[len(nodes)-1].getFirst()
    while f:
        path.insert(0,f)
        f=f.getFrom()
    return [v.realWord for v in path]


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
    HanLP.Config.CoreDictionaryPath=model_path+'.txt'
    HanLP.Config.BiGramDictionaryPath=model_path+'.ngram.txt'
    sent='中国共产党中央委员会总书记，简称“中共中央总书记”，是中国共产党自1982年“中共十二大”以来的最高领导人职务称谓。根据《中国共产党章程（2007年10月21日通过）》规定：“中央委员会总书记负责召集中央政治局会议和中央政治局常务委员会会议，并主持中央书记处的工作。'
    #sent is the sentence that want to segment
    wordnet=generate_wordnet(sent,CoreDictionary.trie)
    print(viterbi(wordnet))
    return ViterbiSegment().enableAllNamedEntityRecognize(False)

if __name__=='__main__':
    corpus_path=r'C:\Users\max21\Desktop\Python\NLP\corpus.txt'#can change other corpus
    model_path=r'C:\Users\max21\Desktop\Python\NLP\model.txt'
    train_bigram(corpus_path,model_path)
    load_bigram(model_path)


