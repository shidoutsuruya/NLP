from pyhanlp import *
import os 

AbstractLexicalAnalyzer = JClass('com.hankcs.hanlp.tokenizer.lexical.AbstractLexicalAnalyzer')
HMMNERecognizer = JClass('com.hankcs.hanlp.model.hmm.HMMNERecognizer')
PerceptronSegmenter = JClass('com.hankcs.hanlp.model.perceptron.PerceptronSegmenter')
PerceptronPOSTagger = JClass('com.hankcs.hanlp.model.perceptron.PerceptronPOSTagger')
Utility = JClass('com.hankcs.hanlp.model.perceptron.utility.Utility')

place_dictionary_path=r'C:\Users\max21\Desktop\Python\NLP\data\dictionary\place'
pku_pos_corpus=r'C:\Users\max21\Desktop\Python\NLP\pku98_pos\199801-train.txt'
save_model=r'C:\Users\max21\Desktop\Python\NLP\named_entity\place'

recognizer = HMMNERecognizer()
recognizer.train(pku_pos_corpus)

word_array = ["东京", "电力", "公司"]  # 构造单词序列
pos_array = ["ns", "n", "n"]  # 构造词性序列
ner_array = recognizer.recognize(word_array, pos_array)  # 序列标注

for word, tag, ner in zip(word_array, pos_array, ner_array):
    print("\n%s\t%s\t%s\t" % (word, tag, ner))

analyzer = AbstractLexicalAnalyzer(PerceptronSegmenter(), PerceptronPOSTagger(), recognizer)
print(analyzer.analyze("东京电力公司秘书来到美国纽约现代艺术博物馆参观"))
scores = Utility.evaluateNER(recognizer, pku_pos_corpus)

