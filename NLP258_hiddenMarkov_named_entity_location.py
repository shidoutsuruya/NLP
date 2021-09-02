from pyhanlp import *
import os 

EasyDictionary = JClass('com.hankcs.hanlp.corpus.dictionary.EasyDictionary')
NSDictionaryMaker = JClass('com.hankcs.hanlp.corpus.dictionary.NSDictionaryMaker')
Sentence = JClass('com.hankcs.hanlp.corpus.document.sentence.Sentence')
DijkstraSegment = JClass('com.hankcs.hanlp.seg.Dijkstra.DijkstraSegment')


place_dictionary_path=r'C:\Users\max21\Desktop\Python\NLP\data\dictionary\place'
pku_pos_corpus=r'C:\Users\max21\Desktop\Python\NLP\pku98_pos\199801-train.txt'
save_model=r'C:\Users\max21\Desktop\Python\NLP\named_entity\place'
def train(corpus, model):
    dictionary = EasyDictionary.create(HanLP.Config.CoreDictionaryPath)  # 核心词典
    maker = NSDictionaryMaker(dictionary)  # 训练模块
    maker.train(corpus)  # 在语料库上训练
    maker.saveTxtTo(model)  # 输出HMM到txt



def load(model):
    HanLP.Config.PlaceDictionaryPath = model+'.txt'  # data/test/ns.txt
    HanLP.Config.PlaceDictionaryTrPath = model+'.tr.txt'
    segment = DijkstraSegment()
    segment.enablePlaceRecognize(True)
    segment.enableCustomDictionary(False)  # 该分词器便于调试
    HanLP.Config.enableDebug()
    print(segment.seg("你是不是黑牛沟村我不管，我是哈佛大学的学生"))


if __name__ == '__main__':
    train(pku_pos_corpus,save_model)
    load(save_model)
   