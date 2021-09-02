from pyhanlp import *
import os 

IOUtil = SafeJClass('com.hankcs.hanlp.corpus.io.IOUtil')
TermFrequency = JClass('com.hankcs.hanlp.corpus.occurrence.TermFrequency')
TermFrequencyCounter = JClass('com.hankcs.hanlp.mining.word.TermFrequencyCounter')
PerceptronLexicalAnalyzer = JClass('com.hankcs.hanlp.model.perceptron.PerceptronLexicalAnalyzer')


counter=TermFrequencyCounter()
counter.add('中国加油，武汉加油')
counter.add('加油，中国队你是嘴巴干')
#statistic use personal segmentor
counter.getSegment().enableIndexMode(True)
counter.setSegment(PerceptronLexicalAnalyzer().enableIndexMode(True))

for term in counter:
    print('%s=%d'%(term.getTerm(),term.getFrequency()))
print(counter.top(2))
string='时的照片,李连杰透露是年轻训练时的照片'
print(TermFrequencyCounter.getKeywordList(string,2))







   
 
   
