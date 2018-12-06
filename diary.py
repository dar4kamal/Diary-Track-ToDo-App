from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import *
from os import path
from time import *
import json
import sys

FORM_CLASS,_=loadUiType(path.join(path.dirname(__file__),"diaryApp.ui"))

class MainApp(QtWidgets.QMainWindow,FORM_CLASS):
    
    def __init__(self,parent=None):
        super(MainApp,self).__init__(parent)
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.handle_ui()
        self.handle_btns()

    def handle_ui(self):
        QtWidgets.QMainWindow.setWindowTitle(self,"Diary App")
        QtWidgets.QMainWindow.setFixedSize(self,350, 400)

    def handle_btns(self):
        self.saveDiary.clicked.connect(self.save)
    
    def save(self):
        pass
        

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
    