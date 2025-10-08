from PyQt6.QtWidgets import QMainWindow, QApplication

from ss05_0810_retail.retail_project.ui.LoginMainWindowEx import LoginMainWindowEx

app=QApplication([])
login_ui=LoginMainWindowEx()
login_ui.setupUi(QMainWindow())
login_ui.showWindow()
app.exec()
