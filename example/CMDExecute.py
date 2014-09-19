__author__ = 'yangh'
#coding=utf-8

import os

os.system("svn")
result = os.popen("ping 192.168.0.3").readline()

print result