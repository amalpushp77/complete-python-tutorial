class Employee:
    employeeNumbers = 0
    employeeScore = 0

    def __init__(self, employeeID, fullName, division):
        self.employeeID = employeeID
        self.fullName = fullName
        self.division = division
        Employee.employeeNumbers += 1

    def incrementScore(self):
        self.employeeScore += 1


e1 = Employee(101, "Amal Pushp", "IT")
print("After creating e1 object")
print("Total no. of employees: ", e1.employeeNumbers)
print("Employee score:", e1.employeeScore)

e2 = Employee(102, "Aditya Gurjar", "R&D")
print("After creating e2 object")
print("Total no. of employees: ", e2.employeeNumbers)
print("Employee score:", e2.employeeScore)

e3 = Employee(103, "Jaideep Mor", "Admin")
print("After creating e3 object")
print("Total no. of employees: ", e3.employeeNumbers)
print("Employee score:", e3.employeeScore)

e3.incrementScore()
print("Score of e3 after using incrementScore() method")
print("Employee score:", e3.employeeScore)
