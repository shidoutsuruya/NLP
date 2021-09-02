from pyhanlp import *
import os

HMMPOSTagger = JClass('com.hankcs.hanlp.model.hmm.HMMPOSTagger')
AbstractLexicalAnalyzer = JClass('com.hankcs.hanlp.tokenizer.lexical.AbstractLexicalAnalyzer')
PerceptronSegmenter = JClass('com.hankcs.hanlp.model.perceptron.PerceptronSegmenter')
FirstOrderHiddenMarkovModel = JClass('com.hankcs.hanlp.model.hmm.FirstOrderHiddenMarkovModel')
SecondOrderHiddenMarkovModel = JClass('com.hankcs.hanlp.model.hmm.SecondOrderHiddenMarkovModel')
POSTrainer = JClass('com.hankcs.hanlp.model.perceptron.POSTrainer')
PerceptronPOSTagger = JClass('com.hankcs.hanlp.model.perceptron.PerceptronPOSTagger')

pku_corpus_train=r'C:\Users\max21\Desktop\Python\NLP\pku98_pos\199801-train.txt'
model=r'C:\Users\max21\Desktop\Python\NLP\pos\MLP_model'

def train_perceptron_pos(corpus,model,string):
    trainer = POSTrainer()
    trainer.train(corpus, model)  # 训练
    tagger = PerceptronPOSTagger(model)  # 加载
    analyzer = AbstractLexicalAnalyzer(PerceptronSegmenter(), tagger)  # 构造词法分析器
    print(analyzer.analyze(string))  # 分词+词性标注




if __name__ == '__main__':
    sentence='斯坦福大学开始深度研究人工智能的发展与应用'
    train_perceptron_pos(pku_corpus_train,model,sentence)
   


