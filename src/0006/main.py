#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

from os import path
from glob import glob
from collections import Counter


if __name__ == '__main__':
    for filename in glob(path.abspath(path.join(path.abspath(__file__), '..', 'diaries', '*.txt'))):
        with open(filename) as f:
            words = f.read().strip().split()
            print("diary {} most important word is {}".format(
                path.basename(filename),
                Counter(words).most_common()[0][0])
            )