from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QTableWidgetItem, QMessageBox

from ss05_0810_retail.retail_project.connectors.employee_connector import EmployeeConnector
from ss05_0810_retail.retail_project.models.employee import Employee
from ss05_0810_retail.retail_project.tests.test_employee_connector import ec
from ss05_0810_retail.retail_project.ui.EmployeeMainWindow import Ui_MainWindow


class EmployeeMainWindowEx(Ui_MainWindow):
    def __init__(self):
        self.ec = EmployeeConnector()
        self.ec.connect()
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.displayEmployeeIntoTable()
        self.setupSignalAndSlot()
    def showWindow(self):
        self.MainWindow.show()
    def displayEmployeeIntoTable(self):
        self.employees = self.ec.get_all_employee()
        #remove emp into table
        self.tableWidget_Employee.setRowCount(0)
        #loading emp into table
        for emp in self.employees:
            #get the last row (for appending)
            row = self.tableWidget_Employee.rowCount()
            #insert a new row (at the last row)
            self.tableWidget_Employee.insertRow(row)
            #insert data for ID column (of row)
            item_id=QTableWidgetItem(str(emp.ID))
            self.tableWidget_Employee.setItem(row, 0, item_id)
            if emp.IsDeleted == 1:
                item_id.setBackground(Qt.GlobalColor.red)
            #Code
            item_code = QTableWidgetItem(str(emp.EmployeeCode))
            self.tableWidget_Employee.setItem(row, 1, item_code)
            #Name
            item_name = QTableWidgetItem(emp.Name)
            self.tableWidget_Employee.setItem(row, 2, item_name)
            #Phone
            item_phone = QTableWidgetItem(emp.Phone)
            self.tableWidget_Employee.setItem(row, 3, item_phone)
            #Email
            item_email = QTableWidgetItem(emp.Email)
            self.tableWidget_Employee.setItem(row, 4, item_email)
    def setupSignalAndSlot(self):
        self.pushButton_New.clicked.connect(self.clear_all)
        self.tableWidget_Employee.itemSelectionChanged.connect(self.show_detail)
        self.pushButton_Save.clicked.connect(self.save_employee)
    def clear_all(self):
        self.lineEdit_ID.setText("")
        self.lineEdit_Code.setText("")
        self.lineEdit_Name.setText("")
        self.lineEdit_Phone.setText("")
        self.lineEdit_Email.setText("")
        self.lineEdit_Code.setFocus()
    def show_detail(self):
        row_index = self.tableWidget_Employee.currentIndex()
        print("You clicked on row ", row_index.row())
        id=self.tableWidget_Employee.item(row_index.row(), 0).text()
        print("Employee ID=",id)
        emp = self.ec.get_detail_infor(id)
        if emp != None:
            self.lineEdit_ID.setText(str(emp.ID))
            self.lineEdit_Code.setText(str(emp.EmployeeCode))
            self.lineEdit_Name.setText(str(emp.Name))
            self.lineEdit_Phone.setText(str(emp.Phone))
            self.lineEdit_Email.setText(str(emp.Email))
            if emp.IsDeleted == 1:
                self.checkBox_IsDeleted.setChecked(True)
            else:
                self.checkBox_IsDeleted.setChecked(False)
    def save_employee (self):
        emp = Employee()
        emp.EmployeeCode = self.lineEdit_Code.text()
        emp.Name = self.lineEdit_Name.text()
        emp.Phone = self.lineEdit_Phone.text()
        emp.Email = self.lineEdit_Email.text()
        emp.Password = self.lineEdit_Password.text()
        emp.IsDeleted = 0

        result = self.ec.insert_one_employee(emp)
        if result > 0:
            self.displayEmployeeIntoTable()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Critical)
            msg.setText("Insert Fail")
            msg.setWindowTitle("Error!!!")
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg.exec()