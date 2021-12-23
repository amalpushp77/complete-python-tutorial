"""
    How to convert traditional code to OOP implementation
        1. Define the parameter used within the nested if statements.
        2. The case expression or the value used for the condition should be converted as a derived class.
        3. The action statement or expressions of the if statement or switch case will be the definition for the method
        present at the derived class.
        4. If the switch case consists of default expression in other languages then that definition will become the
        virtual method at the base class.
        5. If the default expression is not present in switch case then the definition will become the abstract method
        at the base class.
        6. If any common variables are used across all the switch expressions or conditions then that variables will
        become the variables or fields at hte base class.
        """

from abc import ABC, abstractmethod


class Account(ABC):
    def __init__(self, accountNo, customerName, accountType, balance):
        self.AccountNo = accountNo
        self.CustomerName = customerName
        self.AccountType = accountType
        self.Balance = balance

    def __str__(self):
        return f"Account no.: {self.AccountNo} \n" \
               f"Customer Name: {self.CustomerName} \n" \
               f"Account Type: {self.AccountType} \n" \
               f"Balance: {self.Balance} \n"

    def deposit(self, amount):
        self.Balance += amount

    @abstractmethod
    def withdraw(self, amount):
        pass


class SavingsAccount(Account):
    def withdraw(self, amount):
        if self.Balance - amount < 500:
            raise Exception("Insufficient balance")
        else:
            self.Balance -= amount


class CurrentAccount(Account):
    def withdraw(self, amount):
        self.Balance -= amount


sa = SavingsAccount(101, "Amal", "SAVINGS", 15000)
print(sa)
amount = float(input("Enter amount to withdraw: "))
sa.withdraw(amount)
print("Current Balance: ", sa.Balance)

ca = CurrentAccount(102, "Aditya", "CURRENT", 15000)
print(ca)
amount = float(input("Enter amount to withdraw: "))
ca.withdraw(amount)
print("Current Balance: ", ca.Balance)