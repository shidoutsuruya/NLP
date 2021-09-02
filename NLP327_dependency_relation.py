from pyhanlp import *
import os 
KBeamArcEagerDependencyParser = JClass('com.hankcs.hanlp.dependency.perceptron.parser.KBeamArcEagerDependencyParser')
base=r'C:\Users\max21\Desktop\Python\NLP\ctb8.0-dep'
CTB_TRAIN=os.path.join(base,'train.conll')
CTB_DEV = os.path.join(base,'dev.conll')
BROWN_CLUSTER=os.path.join(base,'wiki-cn-cluster.txt')            
CTB_MODEL=os.path.join(base,'ctb.bin')
if __name__ == '__main__':
    parser = KBeamArcEagerDependencyParser.train(CTB_TRAIN, CTB_DEV, BROWN_CLUSTER, CTB_MODEL)
    print(parser.parse("人吃鱼"))

    score = parser.evaluate(CTB_TEST)
    print("UAS=%.1f LAS=%.1f\n" % (score[0], score[1]))
