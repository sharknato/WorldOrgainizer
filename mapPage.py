from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
import sys

class mapPage(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("World Organizer")  
        self.resize(1400, 1100);
        self.setMapUI()
        self.show()
    
    def setMapUI(self):
        menu = QMenuBar(self)
        
        