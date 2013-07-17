# -*- coding: utf-8 -*-

import sys
import thread

from client import TCPConnection

class Core(object):
  def __init__(self):
    self.__connection = TCPConnection()
    self.__loop = True

  def connect(self):
    self.__connection.open()
    thread.start_new_thread(self.__waitMessages())

  def __waitMessages(self):
    while self.__loop:
      data = self.__connection.receive()
      print data

  def send(self, data):
    self.__connection.send(data)

if __name__ == '__main__':
  sys.exit()
