# -*- coding: utf-8 -*-

import sys
import SocketServer
import threading

class server(object):
  def __init__(self):
    self.myPort = 51238 # использовать незарезервированный номер порта

  def run(self):
    myaddr = ('', self.myPort) #'' означает локальный хост
    server = SocketServer.ThreadingTCPServer(myaddr, MyClientHandler)
    self.t = threading.Thread(target=server.serve_forever)

class MyClientHandler(SocketServer.BaseRequestHandler):
  def handle(self): # для каждого клиента
    print 'Новый клиент: ', self.client_address # показать адрес этого клиента
    while True: # self.request – сокет клиента
      data = self.request.recv(1000) # чтение, запись в сокет клиента
      if not data: break
      print 'Сообщение: ', data.decode('utf-8')
      #reply = 'Echo=>%s at %s' % (data, now())
      #self.request.send(reply)
    self.request.close()



if __name__ == '__main__':
  sys.exit()
