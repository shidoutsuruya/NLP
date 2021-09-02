from pyhanlp import *
import os
HMMPOSTagger = JClass('com.hankcs.hanlp.model.hmm.HMMPOSTagger')
AbstractLexicalAnalyzer = JClass('com.hankcs.hanlp.tokenizer.lexical.AbstractLexicalAnalyzer')
PerceptronSegmenter = JClass('com.hankcs.hanlp.model.perceptron.PerceptronSegmenter')
FirstOrderHiddenMarkovModel = JClass('com.hankcs.hanlp.model.hmm.FirstOrderHiddenMarkovModel')
SecondOrderHiddenMarkovModel = JClass('com.hankcs.hanlp.model.hmm.SecondOrderHiddenMarkovModel')
base=os.path.dirname(__file__)
PKU199801_TRAIN=os.path.join(base,'pku98_pos','199801-train.txt')

def GA_train_hmm_pos(corpus, model,string):
    tagger = HMMPOSTagger(model)  
    tagger.train(corpus)  
    analyzer = AbstractLexicalAnalyzer(PerceptronSegmenter(), tagger)  
    print(analyzer.analyze(string)) 



if __name__ == '__main__':
    string='我们开始要用遗传算法标记'
    GA_train_hmm_pos(PKU199801_TRAIN, FirstOrderHiddenMarkovModel(),string)
    


