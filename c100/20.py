#!/usr/bin/python
#!-*- coding:utf-8 -*-

"""
【程序20】
题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
"""

if __name__ == '__main__':
    """
    """
    h = 100
    s = -100
    for i in range(1, 11):
        s += 2 * h
        h /= 2.0

    print s, h

