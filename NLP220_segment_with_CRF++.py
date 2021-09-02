from pyhanlp import *
import os

base=r'C:\Users\max21\Desktop\Python\NLP\CRF++'
original_corpus=r'C:\Users\max21\Desktop\Python\NLP\icwb2-data\testing\msr_test.txt'
model=os.path.join(base,'model')

CWSEvaluator=JClass('com.hankcs.hanlp.seg.common.CWSEvaluator')
CRFSegmenter = JClass('com.hankcs.hanlp.model.crf.CRFSegmenter')
CRFLexicalAnalyzer = JClass('com.hankcs.hanlp.model.crf.CRFLexicalAnalyzer')

def train(corpus,model_loc):
    segmenter = CRFSegmenter()
    segmenter.train(corpus,model_loc)
    return CRFLexicalAnalyzer(segmenter)

segment=train(original_corpus,model)
sents='昔日可以那般北京大兴国际机场'
print(segment.analyzer(sents))
    




