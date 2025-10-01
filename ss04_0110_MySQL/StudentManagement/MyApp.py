import sys

from PyQt6.QtWidgets import QApplication, QMainWindow

from ss04_0110_MySQL.StudentManagement.MainWindowEx import MainWindowEx

app=QApplication([])
myWindow=MainWindowEx()
myWindow.setupUi(QMainWindow())
myWindow.connectMySQL()
myWindow.selectAllStudent()
myWindow.show()
app.exec()