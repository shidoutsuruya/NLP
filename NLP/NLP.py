import jieba
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
from sklearn.datasets import load_files
import os
from sklearn.naive_bayes import BernoulliNB
from sklearn.model_selection import cross_val_score

base=r'C:\Users\max21\Desktop\Python\NLP\movie_appraise'
train_path=os.path.join(base,'train')
test_path=os.path.join(base,'test')

train_set=load_files(train_path) 
test_set=load_files(test_path)

x_train,y_train=train_set.data,train_set.target
x_test,y_test=test_set.data,test_set.target

x_train=[doc.replace(b'<br />',b' ') for doc in x_train]
x_test=[doc.replace(b'<br />',b' ') for doc in x_test]

vect=CountVectorizer().fit(x_train)
x_train_vect=vect.transform(x_train)
print(x_train_vect)

gnb=BernoulliNB()
scores=cross_val_score(gnb,x_train_vect,y_train)
print('score:{:.3f}'.format(scores.mean()))

