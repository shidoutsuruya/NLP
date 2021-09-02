from pyhanlp import *
#Textrank algorithm
content='宝可梦终于完结啦！撒花！感谢大家一路以来的支持！'
keyword_list=HanLP.extractKeyword(content,5)
print(keyword_list)
#phrase algorithm
text='1.熟悉主流机器学习、深度学习框架，如Tensorflow、caffe、Pytorch等，在机器学习和深度学习方面有扎实的理论基础。2.参与过AI相关的大型项目并取得成功，在项目中担任关键技术专家，主导关键技术突破。3.参与过AI平台构建，对AI平台分层设计、关键AI能力建设有深入理解和实践经验。4.对NLP、知识图谱、人物画像、推荐系统、数据处理等相关技术在产品领域内应用有深入理解。'
phrase_list=HanLP.extractPhrase(text,5)
print(phrase_list)

sentence_list=HanLP.extractSummary(text,3)
print(sentence_list)




