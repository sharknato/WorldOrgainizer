from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 

class startWindow(QMainWindow):  
    resized = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setWindowTitle("World Organizer")  
        self.resize(1400, 1100);
        self.setMinimumSize(1200, 900)
        self.UiComponents()
        self.show()
        self.resized.connect(self.onResize)

  
    # method for widgets
    def UiComponents(self):
        self.createMenu()
        
        self.button = QPushButton("Start Button", self)
        #positions and sizes are relative to the window size
        self.button.resize(int(self.width()/10), int(self.height()/15))
        self.button.move(int(self.width()/2 - self.button.width()/2), int(self.height()/3 - self.button.height()/2))
        self.button.clicked.connect(self.clicked)   

    def clicked(self):
        self.newWindow = newWindow()     

    def resizeEvent(self, event):
        self.resized.emit()
        return super(startWindow, self).resizeEvent(event)

    def onResize(self):
        self.button.move(int(self.width()/2 - self.button.width()/2), int(self.height()/3 - self.button.height()/2))

    def createMenu(self):
        self.menuBar = QMenuBar(self)
        self.setMenuBar(self.menuBar)
        #add the menu options
        fileMenu = QMenu("File", self)
        self.menuBar.addMenu(fileMenu)
        editMenu = QMenu("Edit", self)
        self.menuBar.addMenu(editMenu)
        helpMenu = QMenu("Help", self)
        self.menuBar.addMenu(helpMenu)
        #create file menu children
        newAction = QAction("New", fileMenu)
        fileMenu.addAction(newAction)
        saveAction = QAction("Save", fileMenu)
        fileMenu.addAction(saveAction)

# Window that opens to make a new map file
class newWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("New Map")  
        self.resize(600,400);
        self.setMinimumSize(600, 400)
        self.setMaximumSize(600, 400)
        #self.UiComponents()
        self.show()


class mapWindow(QMainWindow):
    resized = QtCore.pyqtSignal()

