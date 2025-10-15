from ss05_0810_retail.retail_project.connectors.employee_connector import EmployeeConnector
from ss05_0810_retail.retail_project.models.employee import Employee

ec = EmployeeConnector()
ec.connect()
emp=Employee()
emp.EmployeeCode="EMP888"
emp.Name="Doraemon"
emp.Phone="456"
emp.Email="doraemon@gmail.com"
emp.IsDeleted=0
emp.Password="456"

result = ec.insert_one_employee(emp)
if result>0:
    print("Inserted Employee successfully")
else:
    print("Inserted Employee failed")
