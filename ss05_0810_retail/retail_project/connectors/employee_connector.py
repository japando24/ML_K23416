from ss05_0810_retail.retail_project.connectors.connector import Connector
from ss05_0810_retail.retail_project.models.employee import Employee


class EmployeeConnector (Connector):
    def login(self, email, pwd):
        sql = "SELECT * FROM employee WHERE Email=%s AND Password=%s"
        val = (email, pwd)
        dataset = self.fetchone(sql, val)
        if dataset is None:
            return None
        emp = Employee (dataset[0], dataset[1],
                        dataset[2], dataset[3],
                        dataset[4], dataset[5], dataset[6])
        return emp