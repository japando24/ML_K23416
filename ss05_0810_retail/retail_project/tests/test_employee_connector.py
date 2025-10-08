from ss05_0810_retail.retail_project.connectors.employee_connector import EmployeeConnector

ec = EmployeeConnector()
ec.connect()
em=ec.login("johndo24@gmail.com","24042004")
if em == None:
    print("Login Failed")
else:
    print("Login Succeeded")
    print(em)