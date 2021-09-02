from pyhanlp import *
import os
CRFSegmenter = JClass('com.hankcs.hanlp.model.crf.CRFSegmenter')
crf=JClass('com.hankcs.hanlp.model.crf.crfpp.crf_learn')
print(crf)

base=r'C:\Users\max21\Desktop\Python\NLP\CRF++'
original_corpus=os.path.join(base,'corpus.txt')
test_data=os.path.join(base,'test.txt')

TXT_CORPUS_PATH = original_corpus
TSV_CORPUS_PATH = TXT_CORPUS_PATH + ".tsv"
TEMPLATE_PATH = base + "\\cws-template.txt"
CRF_MODEL_PATH = base + "\\crf-cws-model"
CRF_MODEL_TXT_PATH = base + "\\crf-cws-model.txt"


def train_or_load(corpus_txt_path=TXT_CORPUS_PATH, model_txt_path=CRF_MODEL_TXT_PATH):
    if os.path.isfile(model_txt_path):  # 已训练，直接加载
        segmenter = CRFSegmenter(model_txt_path)
        return segmenter
    else:
        segmenter = CRFSegmenter()  # 创建空白分词器
        segmenter.convertCorpus(corpus_txt_path, TSV_CORPUS_PATH)  # 执行转换
        segmenter.dumpTemplate(TEMPLATE_PATH)  # 导出特征模板
        # 交给CRF++训练
        print("corpus convert %s ，feature template %s" % (TSV_CORPUS_PATH, TEMPLATE_PATH))
        print( " -f 3 -c 4.0 %s %s %s -t" % ( TEMPLATE_PATH, TSV_CORPUS_PATH, CRF_MODEL_PATH))
        print('crf start')


if __name__ == '__main__':
    segment = train_or_load()
    print('load finish')
    if segment:
        print(segment.segment("商品和服务"))

