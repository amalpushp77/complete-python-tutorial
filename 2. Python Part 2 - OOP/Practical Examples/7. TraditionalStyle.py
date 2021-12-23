# create a bank account. Saving account with minimum 500 balance and current account with no minimum balance.

accountNo = input("enter Account Number: ")
customerName = input("Enter Customer Name: ")
accountType = input("Enter Account Type: ")
balance = float(input("Enter Balance: "))


def showAccount():
    print(f"Account: {accountNo} \n"
          f"Customer Name: {accountType} \n"
          f"Account Type: {accountType} \n"
          f"Balance: {balance}")


def withdraw(balance, amount, accountType):
    if accountType == "SAVINGS":
        new_balance = balance - amount
        if new_balance < 500:
            raise Exception("Insufficient Balance")
        else:
            balance = new_balance
            return balance
    elif accountType == "CURRENT":
        balance = balance - amount
        return balance


showAccount()
amount = float(input("Enter amount to be withdraw: "))
type = "SAVINGS"
balance = withdraw(balance, amount, type)
print("After withdrawing")
showAccount()
