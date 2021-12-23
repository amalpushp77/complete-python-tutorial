import datetime
import calendar


class PayrollManagementSystem:

    def calculate_payroll(self, employees):
        print("Payroll Management System")
        print("+++++++++++++++++++++++++++++++++")

        for employee in employees:
            print(f"Employee: {employee.id} \n"
                  f"Employee Name: {employee.name} \n"
                  f"Amount: {employee.calculate_payroll()}")
            print("----------------------------")


class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class SalaryEmployee(Employee):
    def __init__(self, id, name, rate_per_day):
        Employee.__init__(self, id, name)
        self.rate_per_day = rate_per_day

    def calculate_payroll(self):
        today = datetime.datetime.now()
        totaldays = calendar.monthrange(today.year, today.month)[1]
        return self.rate_per_day * totaldays


class PartTimeEmployee(Employee):
    def __init__(self, id, name, total_hours, rate_per_hour):
        Employee.__init__(self, id, name)
        self.total_hours = total_hours
        self.rate_per_hour = rate_per_hour

    def calculate_payroll(self):
        return self.total_hours * self.rate_per_hour


class CommissionEmployee(SalaryEmployee):
    def __init__(self, id, name, rate_per_day, commission):
        SalaryEmployee.__init__(self, id, name, rate_per_day)
        self.commission = commission

    def calculate_payroll(self):
        salary = SalaryEmployee.calculate_payroll(self)
        return salary + self.commission
