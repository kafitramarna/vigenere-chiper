import sys,os
from PyQt5.QtWidgets import QApplication,QDialog
from PyQt5.uic import loadUi
from controllers.HomeController import HomeController

if getattr(sys, 'frozen', False):
    os.chdir(sys._MEIPASS)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainMenu = HomeController() 
    mainMenu.show()
    sys.exit(app.exec_())