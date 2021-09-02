from pyhanlp import *
import random

ClusterAnalyzer = JClass('com.hankcs.hanlp.mining.cluster.ClusterAnalyzer')
analyzer= ClusterAnalyzer() 
def add_text(name,ran_num):   
    lst=[chr(random.randint(97,100)) for i in range(ran_num)]
    combine=','.join(lst)
    print(name,':',combine)
    analyzer.addDocument(name,combine)

name_list=['Max','John','Pizza','Roman','PHALI','Huis','Prso']
for name in name_list:
    add_text(name,20)

print(analyzer.kmeans(3))
print(analyzer.repeatedBisection(1.))



ClusterAnalyzer = JClass('com.hankcs.hanlp.mining.cluster.ClusterAnalyzer')
sogou_corpus_path=r'C:\Users\max21\Desktop\Python\NLP\sougo_corpus'
if __name__ == '__main__':
    for algorithm in "kmeans", "repeated bisection":
        print("%s F1=%.2f\n" % (algorithm, ClusterAnalyzer.evaluate(sogou_corpus_path, algorithm) * 100))
