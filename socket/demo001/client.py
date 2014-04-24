#!/usr/bin/python
#coding=utf-8

import socket,time

HOST = '127.0.0.1'
PORT=8000
#s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.connect((HOST,PORT))

while 1:
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST,PORT))
    cmd=raw_input().strip()
    s.sendall(cmd)
    data=s.recv(1024)
    print(data)
    s.close()

