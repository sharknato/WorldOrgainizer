from view import *
import sys

App = QApplication(sys.argv)
# assign stylesheet
App.setStyleSheet(open('styles.css').read())

#creates a startwindow from view.py
window = startWindow()

# start the app
sys.exit(App.exec())