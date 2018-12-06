from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime
from PyQt5.uic import *
from os import path
from time import *
import json
import sys
import os

FORM_CLASS,_=loadUiType(path.join(path.dirname(__file__),"diaryApp.ui"))

class MainApp(QtWidgets.QMainWindow,FORM_CLASS):
    
    def __init__(self,parent=None):
        super(MainApp,self).__init__(parent)
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.globals()
        self.handle_ui()
        self.handle_btns()        

    def globals(self):
        self.fileName = "data.json"

    def handle_ui(self):
        QtWidgets.QMainWindow.setWindowTitle(self,"Diary App")
        QtWidgets.QMainWindow.setFixedSize(self,350, 400)

    def handle_btns(self):
        self.saveDiary.clicked.connect(self.save)
    
    def getData(self):
        try:
            with open(self.fileName, mode='r') as f:
                data = json.load(f)
        except:
            if os.path.exists(self.fileName):
                os.remove(self.fileName)
            with open(self.fileName, mode='w') as f:
                json.dump([], f)
            with open(self.fileName, mode='r') as f:
                data = json.load(f)
        return data

    def save(self):
                
        data = self.getData()
        output = {
            "content":str(self.editDiary.document().toPlainText()),
            "date":str(datetime.now().date()),
            "time":str(strftime("%H:%M:%S"))
        }
        data.append(output)        
        with open(self.fileName, mode='w') as f:
            json.dump(data, f)
        

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
    