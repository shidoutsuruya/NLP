# cncorpus

## Introduction

Chinese Word Segmentation and Part-of-Speech Tagging corpus on Internet novel “Zhuxian”.

Converted from original dataset for paper [Type-Supervised Domain Adaptation for Joint Segmentation and POS-Tagging](http://www.aclweb.org/anthology/E/E14/E14-1062.pdf).

## How to Get It?

```bash
wget https://zhangmeishan.github.io/eacl14mszhang.zip
unzip eacl14mszhang.zip
python3 make
```

You'll get 3 `.txt` files in this folder. The format follows PKU, one sample from the `train.txt` is:

```text
第一/OD 章/M 隐忧/NN
张小凡/NR 看着/VV 前方/NN 那/DT 个/M 中年/NN 文士/NN ，/PU 也/AD 就/AD 是/VC 当今/NT 正道/NN 的/DEG 心腹大患/NN “/PU 鬼王/NR ”/PU ，/PU 脑海/NN 中/LC 一/CD 片/M 混乱/NN 。/PU
```

## License

Only for research and educational purpose. Proper citation is required in scientific publications.

```latex
@article{zhang2014type-supervised,
title={Type-Supervised Domain Adaptation for Joint Segmentation and POS-Tagging},
author={Zhang, Meishan and Zhang, Yue and Che, Wanxiang and Liu, Ting},
pages={588--597},
year={2014}}
```