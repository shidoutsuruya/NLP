from pyhanlp import *
import os 

IOUtil = SafeJClass('com.hankcs.hanlp.corpus.io.IOUtil')
text_path=r'C:\Users\max21\Desktop\Python\NLP\four_classical\three_kingdom.txt'
corpus=IOUtil.newBufferedReader(text_path)
word_info_list=HanLP.extractWords(corpus,100,True)
print(word_info_list)
  





   
 
   
