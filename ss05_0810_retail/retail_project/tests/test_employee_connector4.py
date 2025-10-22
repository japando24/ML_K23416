from ss05_0810_retail.retail_project.connectors.employee_connector import EmployeeConnector
from ss05_0810_retail.retail_project.models.employee import Employee

ec = EmployeeConnector()
ec.connect()
emp=Employee()
emp.ID=6

result = ec.delete_one_employee(emp)
if result > 0:
    print("Deleted Employee successfully")
else:
    print("Deleted Employee failed")
