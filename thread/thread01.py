#!/usr/bin/env python
import threading

class mythread(threading.Thread):
    def __init__(self,threadname):
        threading.Thread.__init__(self,name=threadname)
    def run(self):
        print self.getName()
t1=mythread('t1')
t1.start()

