from pyhanlp import *
print(HanLP.segment('hello world'))
for term in HanLP.segment('要下于了，赶快躲起来'):
    print('{}\t{}'.format(term.word,term.nature))

testCase=['疫情形势依然严峻','社会各界仍在全力应战。','与全民皆兵的氛围极不相称的是']
for i in testCase:
    print(HanLP.segment(i))
print('capture key word:')
document=testCase[1]
print(HanLP.extractKeyword(document,2))
print(HanLP.parseDependency(testCase[2]))
