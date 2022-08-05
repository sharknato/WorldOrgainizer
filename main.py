from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
from mapPage import *
import sys

  
class Window(QMainWindow):
  
    def __init__(self):
        super().__init__()
        self.setWindowTitle("World Organizer")  
        self.resize(1400, 1100);
        self.UiComponents()
        self.show()
  
    # method for widgets
    def UiComponents(self):
        button = QPushButton("Start Button", self)
        #positions and sizes are relative to the window size
        button.resize(int(self.width()/10), int(self.height()/15))
        button.move(int(self.width()/2 - button.width()/2), int(self.height()/3 - button.height()/2))
  
App = QApplication(sys.argv)

# assign stylesheet
App.setStyleSheet(open('styles.css').read())
  
window = Window()
  
# start the app
sys.exit(App.exec())