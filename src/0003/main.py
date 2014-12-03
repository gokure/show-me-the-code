#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# pip install redis
#

import random
import string
import redis

def friendly_token(chars=None, length=8):
    if chars is None:
        chars = string.ascii_uppercase + string.digits
    return ''.join(random.SystemRandom().choice(chars) for _ in range(length))


if __name__ == '__main__':
    discounts = [friendly_token(chars=string.digits, length=6) for x in xrange(200)]

    r = redis.StrictRedis(host='localhost',port=6379, db=0)

    print r.sadd('smtc:0003:discounts', *discounts)
