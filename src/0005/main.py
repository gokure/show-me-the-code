#!/usr/bin/env python
# -*- coding: utf-8 -*-

# pip install PIL

from os import path
from glob import glob
from PIL import Image

def image_resize(filename):
    max_height, max_width = 1136, 640 # iPhone 5' screen is
    try:
        with Image.open(filename) as img:
            raw_width, raw_height = img.size
            width_ratio = float(max_width) / raw_width if raw_width > max_width else 1
            height_ratio = float(max_height) / raw_height if raw_height > max_height else 1
            ratio = width_ratio if height_ratio > width_ratio else height_ratio
            new_width = int(raw_width*ratio)
            new_height = int(raw_height*ratio)
            img.resize((new_width, new_height), Image.ANTIALIAS).save(filename, quality=95)
    except IOError:
        print "The file {0} is not picture.".format(path.basename(filename))

if __name__ == '__main__':
    for filename in glob(path.abspath(path.join(path.abspath(__file__), '..', 'images', '*'))):
        image_resize(filename)