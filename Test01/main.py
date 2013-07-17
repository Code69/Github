# -*- coding: utf-8 -*-

import sys
import ui 

def main():
  userInterface = ui.ConsoleUI()
  try:
    userInterface.cmdloop()
  except KeyboardInterrupt:
    print "завершение сеанса..."

if __name__ != '__main__':
  sys.exit()

main()
