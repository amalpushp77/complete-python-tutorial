import payroll

semp = payroll.SalaryEmployee(101, "Amal", 1000)
pemp = payroll.PartTimeEmployee(102, "Aditya", 40, 50)
cemp = payroll.CommissionEmployee(103, "Jaideep", 1000, 1500)

payroll_system = payroll.PayrollManagementSystem()
payroll_system.calculate_payroll([semp, pemp, cemp])


