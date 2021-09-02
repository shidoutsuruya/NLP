from pyhanlp import *
import os 


place_dictionary_path=r'C:\Users\max21\Desktop\Python\NLP\data\dictionary\place'
pku_pos_corpus=r'C:\Users\max21\Desktop\Python\NLP\pku98_pos\199801-train.txt'
save_model=r'C:\Users\max21\Desktop\Python\NLP\named_entity\new_tag'
pku_pos_corpus_test=r'C:\Users\max21\Desktop\Python\NLP\pku98_pos\199801-test.txt'
base=r'C:\Users\max21\Desktop\Python\NLP\plane-re'
plane_corpus=os.path.join(base,'train.txt')
plane_model=os.path.join(base,'plane_model.bin')

NERTrainer = JClass('com.hankcs.hanlp.model.perceptron.NERTrainer')
PerceptronNERecognizer = JClass('com.hankcs.hanlp.model.perceptron.PerceptronNERecognizer')
PerceptronSegmenter = JClass('com.hankcs.hanlp.model.perceptron.PerceptronSegmenter')
PerceptronPOSTagger = JClass('com.hankcs.hanlp.model.perceptron.PerceptronPOSTagger')
Sentence = JClass('com.hankcs.hanlp.corpus.document.sentence.Sentence')
Utility = JClass('com.hankcs.hanlp.model.perceptron.utility.Utility')
AbstractLexicalAnalyzer = JClass('com.hankcs.hanlp.tokenizer.lexical.AbstractLexicalAnalyzer')
CWSTrainer = JClass('com.hankcs.hanlp.model.perceptron.CWSTrainer')

if __name__ == '__main__':
    trainer = NERTrainer()
    trainer.tagSet.nerLabels.clear()  # 不识别nr、ns、nt
    trainer.tagSet.nerLabels.add("np")  # 目标是识别np
    #Named Entity Recognition(NER) training
    print('NER TRAINING START!!!!')
    recognizer = PerceptronNERecognizer(trainer.train(plane_corpus, plane_model).getModel())
    #Cognition Word Segment training
    print('CWS TRAINING START!!!!')
    CWS_MODEL = CWSTrainer().train(plane_corpus, plane_model.replace('plane_model.bin', 'segment_model.bin')).getModel()
    analyzer = AbstractLexicalAnalyzer(PerceptronSegmenter(CWS_MODEL), PerceptronPOSTagger(), recognizer)
    print(analyzer.analyze("米高扬设计米格-17PF：米格-17PF型战斗机比米格-17P性能更好。"))
    print(analyzer.analyze("米格-阿帕奇-666S横空出世。"))


   
 
   
