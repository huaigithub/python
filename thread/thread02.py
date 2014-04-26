#!/usr/bin/env python
#coding=utf8

import threading

def loop2():
    for i in range(10000,20000000000):
       print i
def loop():
    for i in range(1,10000):
        print i

t = threading.Thread(target=loop)
t2=threading.Thread(target=loop2)

t.start()
t2.start()


t1.join()
t2.join()

