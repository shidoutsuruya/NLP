from pyhanlp import *
import os 

WEIBO_PATH=r'C:\Users\max21\Desktop\Python\NLP\weibo-classification'

for folder in os.listdir(WEIBO_PATH):
    big_text = ""
    print(folder)
    for file in os.listdir(os.path.join(WEIBO_PATH, folder)):
        with open(os.path.join(WEIBO_PATH, folder, file),encoding='utf-8') as src:
                 big_text += "".join(src.readlines())
        #open every txt
        word_info_list = HanLP.extractWords(big_text, 10)
        print(word_info_list)
                
  





   
 
   
