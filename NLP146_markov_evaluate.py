from pyhanlp import *
import os

CWSTrainer = JClass('com.hankcs.hanlp.model.perceptron.CWSTrainer')
PerceptronLexicalAnalyzer = JClass('com.hankcs.hanlp.model.perceptron.PerceptronLexicalAnalyzer')
LinearModel = JClass('com.hankcs.hanlp.model.perceptron.model.LinearModel')
Segment = JClass('com.hankcs.hanlp.seg.Segment')
CWSEvaluator = JClass('com.hankcs.hanlp.seg.common.CWSEvaluator')

sighan05=r'C:\Users\max21\Desktop\Python\NLP\icwb2-data'
msr_dict = os.path.join(sighan05, 'gold', 'msr_training_words.utf8')
msr_train = os.path.join(sighan05, 'training', 'msr_training.utf8')
msr_model = os.path.join(r'C:\Users\max21\Desktop\Python\NLP\model', 'msr_cws')
msr_test = os.path.join(sighan05, 'testing', 'msr_test.utf8')
msr_output = os.path.join(sighan05, 'testing', 'msr_bigram_output.txt')
msr_gold = os.path.join(sighan05, 'gold', 'msr_test_gold.utf8')

def trainStructuredPerceptron():
    model = CWSTrainer().train(msr_train, msr_train, msr_model, 0., 10, 8).getModel()
    return PerceptronLexicalAnalyzer(model).enableCustomDictionary(False)


def trainAveragedPerceptron():
    model = CWSTrainer().train(msr_train, msr_train, msr_model, 0., 10, 1).getModel()
    return PerceptronLexicalAnalyzer(model).enableCustomDictionary(False)

#print("结构化感知机")
#print(CWSEvaluator.evaluate(trainStructuredPerceptron(), msr_test, msr_output, msr_gold, msr_dict))
#print("平均感知机")
#print(CWSEvaluator.evaluate(trainAveragedPerceptron(), msr_test, msr_output, msr_gold, msr_dict))


segment=PerceptronLexicalAnalyzer(msr_model).enableCustomDictionary(False)
sent='习近平与川普通电话用四川普通话探讨银川普通高考'
sent2='出席会议的有习近平和他妻子，川普探讨银川和他的一家人，安倍等领导人'
print('originally:')
print(segment.seg(sent))
for i in range(3):
    segment.learn('有 习近平')
    segment.learn('与 川普 通 电话')
print('learned')
print(segment.seg(sent2))