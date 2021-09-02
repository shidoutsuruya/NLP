# -*- coding:utf-8 -*-
# Author：hankcs
# Date: 2018-06-07 21:54
import os


def convert(src_path, dst_path):
    with open(src_path) as src, open(dst_path, 'w') as out:
        for line in src:
            if line.startswith('#'):
                continue
            line = line.strip()
            if len(line) == 0:
                out.write(os.linesep)
            else:
                cells = line.split()
                out.write('{}/{} '.format(cells[1], cells[3]))


if __name__ == '__main__':
    convert('UD_Japanese-GSD/ja_gsd-ud-train.conllu', 'ja_gsd-ud-train.txt')
    convert('UD_Japanese-GSD/ja_gsd-ud-dev.conllu', 'ja_gsd-ud-dev.txt')
    convert('UD_Japanese-GSD/ja_gsd-ud-test.conllu', 'ja_gsd-ud-test.txt')
