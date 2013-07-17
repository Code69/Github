# -*- coding: utf-8 -*-

import sys
import socket

class TCPConnection(object):
  def __init__(self):
    self.__serverAddress = ('127.0.0.1', 51238)
    pass

  def __del__(self):
    self.__connection.close()

  def setServerAddress(self, ip, port):
    self.__serverAddress = (ip, port)

  def open(self):
    self.__connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.__connection.connect(self.__serverAddress)

  def close(self):
    self.__connection.close()

  def send(self, data):
    self.__connection.send(data)

  def receive(self):
    data = self.__connection.recv(1024)
    return data

if __name__ == '__main__':
  sys.exit()
