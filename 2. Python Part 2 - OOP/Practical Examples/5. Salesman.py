class Employee:
    employeeNumbers = 0
    employeeScore = 0

    def __init__(self, employeeID, fullName, division):
        self.employeeID = employeeID
        self.fullName = fullName
        self.division = division

    def showEmp(self):
        print(f"Employee ID: {self.employeeID} \n"
              f"Name: {self.fullName} \n"
              f"Division: {self.division}")


class Salesman(Employee):

    def __init__(self, employeeID, fullName, division, team):
        Employee.__init__(self, employeeID, fullName, division)
        self.team = team

    # # method overriding
    # def showEmp(self):
    #     Employee.showEmp()
    #     print(f"Team Name: {e1.team}")


e1 = Salesman(101, "Amal Pushp", "IT", "PythonDQ")
e1.showEmp()
print(f"Team Name: {e1.team}")
