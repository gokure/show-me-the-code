#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import string

def friendly_token(chars=None, length=8):
    if chars is None:
        chars = string.ascii_uppercase + string.digits
    return ''.join(random.SystemRandom().choice(chars) for _ in range(length))


if __name__ == '__main__':
    for x in xrange(200):
        print friendly_token(chars=string.digits, length=6)