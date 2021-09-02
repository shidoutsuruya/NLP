from pyhanlp import *

CoNLLSentence = JClass('com.hankcs.hanlp.corpus.dependency.CoNll.CoNLLSentence')
CoNLLWord = JClass('com.hankcs.hanlp.corpus.dependency.CoNll.CoNLLWord')
IDependencyParser = JClass('com.hankcs.hanlp.dependency.IDependencyParser')
NeuralNetworkDependencyParser = JClass('com.hankcs.hanlp.dependency.nnparser.NeuralNetworkDependencyParser')

if __name__ == '__main__':
    parser = NeuralNetworkDependencyParser()
    sentence = parser.parse("徐先生还具体帮助他确定了把画雄鹰、松鼠和麻雀作为主攻目标。")
    print(sentence)
    for word in sentence.iterator():  # 通过dir()可以查看sentence的方法
        print("%s --(%s)--> %s" % (word.LEMMA, word.DEPREL, word.HEAD.LEMMA))
    print()

    # 也可以直接拿到数组，任意顺序或逆序遍历
    word_array = sentence.getWordArray()
    for word in word_array:
        print("%s --(%s)--> %s" % (word.LEMMA, word.DEPREL, word.HEAD.LEMMA))
    print()

    # 还可以直接遍历子树，从某棵子树的某个节点一路遍历到虚根
    CoNLLWord = JClass("com.hankcs.hanlp.corpus.dependency.CoNll.CoNLLWord")
    head = word_array[12]
    while head.HEAD:
        head = head.HEAD
        if (head == CoNLLWord.ROOT):
            print(head.LEMMA)
        else:
            print("%s --(%s)--> " % (head.LEMMA, head.DEPREL))
