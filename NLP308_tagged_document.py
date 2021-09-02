from pyhanlp import *
AbstractDataSet = JClass('com.hankcs.hanlp.classification.corpus.AbstractDataSet')
Document = JClass('com.hankcs.hanlp.classification.corpus.Document')
FileDataSet = JClass('com.hankcs.hanlp.classification.corpus.FileDataSet')
MemoryDataSet = JClass('com.hankcs.hanlp.classification.corpus.MemoryDataSet')
weibo_path=r'C:\Users\max21\Desktop\Python\NLP\weibo-classification'

if __name__ == '__main__':
    dataSet = MemoryDataSet() 
    dataSet.load(weibo_path) 
#plus new class
    dataSet.add("自然语言处理",'自然语言处理有一些趣味')
    allClasses = dataSet.getCatalog().getCategories()  
    print("type：%s" % (allClasses))
#show all the article type
    for document in dataSet.iterator():
        print("this article type：" + allClasses.get(document.category))
        break
        
