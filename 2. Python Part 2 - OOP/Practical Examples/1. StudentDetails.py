class Name:
    def __init__(self, firstName, middleName, lastName):
        self.firstName = firstName
        self.middleName = middleName
        self.lastname = lastName


class Student:
    def __init__(self, rollNo, fullName, course):
        self.rollNo = rollNo
        self.fullName = fullName
        self.course = course


s1 = Student(101, Name("Aditya", "Makrand", "Gurjar"), "OOP with python")
s2 = Student(101, Name("Amal", "", "Pushp"), "python")

students = [s1, s2]

for student in students:
    print(f"Roll number: {student.rollNo} \n"
          f"Student name: {student.fullName.firstname} {student.fullName.middleName} {student.fullName.lastName} \n"
          f"Course enrolled: {student.course}")
