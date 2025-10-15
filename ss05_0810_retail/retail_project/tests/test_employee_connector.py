from ss05_0810_retail.retail_project.connectors.employee_connector import EmployeeConnector

ec = EmployeeConnector()
ec.connect()
em=ec.login("johndo24@gmail.com","24042004")
if em == None:
    print("Login Failed")
else:
    print("Login Succeeded")
    print(em)

#Test get all employee
print("List of Employee")
ds=ec.get_all_employee()
print(ds)
for emp in ds:
    print(emp)

id=1
emp = ec.get_detail_infor(id)
if emp == None:
    print("Employee Not Found")
else:
    print("Employee Found")
    print(emp)