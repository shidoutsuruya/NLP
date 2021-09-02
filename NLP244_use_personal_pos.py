from pyhanlp import *
import os

CustomDictionary.insert("苹果", "手机品牌 1")
CustomDictionary.insert("iPhone X", "手机型号 1")
analyzer = PerceptronLexicalAnalyzer()
analyzer.enableCustomDictionaryForcing(True)
print(analyzer.analyze("你们苹果iPhone X保修吗？"))
print(analyzer.analyze("多吃苹果有益健康"))

HMMPOSTagger = JClass('com.hankcs.hanlp.model.hmm.HMMPOSTagger')
AbstractLexicalAnalyzer = JClass('com.hankcs.hanlp.tokenizer.lexical.AbstractLexicalAnalyzer')
PerceptronSegmenter = JClass('com.hankcs.hanlp.model.perceptron.PerceptronSegmenter')
POSTrainer = JClass('com.hankcs.hanlp.model.perceptron.POSTrainer')
PerceptronPOSTagger = JClass('com.hankcs.hanlp.model.perceptron.PerceptronPOSTagger')

zhuxian_corpus=r'C:\Users\max21\Desktop\Python\NLP\zhuxian\train.txt'
model=r'C:\Users\max21\Desktop\Python\NLP\zhuxian\zhuxian_model'

def train_perceptron_pos(corpus,model,string):
    trainer = POSTrainer()
    trainer.train(corpus, model) 
    tagger = PerceptronPOSTagger(model)  
    analyzer = AbstractLexicalAnalyzer(PerceptronSegmenter(), tagger)  
    print(analyzer.analyze(string)) 



string="陆雪琪的天琊神剑不做丝毫退避，直冲而上，瞬间，这两道奇光异宝撞到了一起。" 
train_perceptron_pos(zhuxian_corpus,model,string)  
