from pyhanlp import *
import os

HMMPOSTagger = JClass('com.hankcs.hanlp.model.hmm.HMMPOSTagger')
AbstractLexicalAnalyzer = JClass('com.hankcs.hanlp.tokenizer.lexical.AbstractLexicalAnalyzer')
PerceptronSegmenter = JClass('com.hankcs.hanlp.model.perceptron.PerceptronSegmenter')
FirstOrderHiddenMarkovModel = JClass('com.hankcs.hanlp.model.hmm.FirstOrderHiddenMarkovModel')
SecondOrderHiddenMarkovModel = JClass('com.hankcs.hanlp.model.hmm.SecondOrderHiddenMarkovModel')
POSTrainer = JClass('com.hankcs.hanlp.model.perceptron.POSTrainer')
PerceptronPOSTagger = JClass('com.hankcs.hanlp.model.perceptron.PerceptronPOSTagger')
CRFPOSTagger = JClass('com.hankcs.hanlp.model.crf.CRFPOSTagger')

pku_corpus_train=r'C:\Users\max21\Desktop\Python\NLP\pku98_pos\199801-train.txt'
model=r'C:\Users\max21\Desktop\Python\NLP\pos\CFR_model'

def train_crf_pos(corpus,model,string):
    tagger = CRFPOSTagger(None)  
    tagger.train(corpus, model)  
    tagger = CRFPOSTagger(model) 
    analyzer = AbstractLexicalAnalyzer(PerceptronSegmenter(), tagger)  
    print(analyzer.analyze(string))  



if __name__ == '__main__':
    string='北京的大学之中以北京大学为标准，其排名也没有进QS30名的位置，\
    而哈佛大学则是全世界最好的大学，没有之一。'
    train_crf_pos(pku_corpus_train,model,string)


