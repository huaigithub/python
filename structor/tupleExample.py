# -*- coding:utf-8 -*-
__author__ = 'yangh'

tup001 = tuple(['a','b','c'])
tup002 = tuple('ab')
print tup001
print tup002

bbs = [('a','b','c')]

for (k,v,c) in bbs:
    print k
    print v
    print c
