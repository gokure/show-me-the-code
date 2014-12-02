#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# pip install MySQL-python
#
# # create table
#
# CREATE TABLE `coupons` (
#     `id` INT(11) NOT NULL AUTO_INCREMENT,
#     `discount` VARCHAR(50) NOT NULL,
#     PRIMARY KEY (`id`),
#     UNIQUE INDEX `discount` (`discount`)
# )
# COLLATE='utf8_general_ci'
# ENGINE=InnoDB;


import random
import string
import MySQLdb

def friendly_token(chars=None, length=8):
    if chars is None:
        chars = string.ascii_uppercase + string.digits
    return ''.join(random.SystemRandom().choice(chars) for _ in range(length))


if __name__ == '__main__':
    discounts = [(friendly_token(chars=string.digits, length=6),) for x in xrange(200)]

    db = MySQLdb.connect(user='user', passwd='password', db='test', charset='utf8')
    c = db.cursor()

    try:
        c.executemany("INSERT INTO `coupons` (`discount`) VALUES (%s)", discounts)
        db.commit()
    except:
        db.rollback()

    db.close()
