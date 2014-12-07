#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

from os import path

if __name__ == '__main__':
    with open(path.join(path.abspath(__file__), '..', 'example.txt')) as f:
        words = f.read().strip().split()
        print(len(words))