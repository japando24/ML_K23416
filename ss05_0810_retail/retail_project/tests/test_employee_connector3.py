from ss05_0810_retail.retail_project.connectors.employee_connector import EmployeeConnector
from ss05_0810_retail.retail_project.models.employee import Employee

ec = EmployeeConnector()
ec.connect()
emp=Employee()
emp.ID=7
emp.EmployeeCode="EMP111"
emp.Name="QC"
emp.Phone="456"
emp.Email="doraemon@gmail.com"
emp.IsDeleted=0
emp.Password="456"

result = ec.update_one_employee(emp)
if result>0:
    print("Updated Employee successfully")
else:
    print("Updated Employee failed")
