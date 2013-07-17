# -*- coding: utf-8 -*-

import sys
import cmd
import server


class ConsoleUI(cmd.Cmd):
  def __init__(self):
    cmd.Cmd.__init__(self)
    self.prompt = ">> "
    self.intro  = "Для справки наберите 'help'"
    self.doc_header ="Доступные команды (для справки по конкретной команде наберите 'help _команда_')"

  def default(self, line):
    print "Несуществующая команда"
  def do_say (self, line):
    from socket import *
    serverHost = '10.85.136.43'  # имя сервера, например: 'starship.python.net'
    serverPort = 51238        # незарезервированный порт, используемый сервером
    sockobj = socket(AF_INET, SOCK_STREAM)      # создать объект сокета TCP/IP
    sockobj.connect((serverHost, serverPort))   # соединение с сервером и портом
    sockobj.send(line.encode('utf-8'))               # послать серверу строчку через сокет
    #data = sockobj.recv(1000)        # получить строку от сервера: до 1k
    #print 'Client received:', data.decode('utf-8')
    sockobj.close()
  def do_server(self, port):
    serv = server.server()
    serv.run()

  def do_exit(self, args):
    sys.exit()


if __name__ == '__main__':
  sys.exit()
