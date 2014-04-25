#!/usr/bin/env python3
#coding=utf-8

import socket,os,SocketServer

class TCPHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).strip()
        print "{} wrote:", format(self.client_address[0])
        self.request.sendall(self.data.upper())

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    server = SocketServer.ThreadingTCPServer((HOST,PORT), TCPHandler)
    server.serve_forever()

