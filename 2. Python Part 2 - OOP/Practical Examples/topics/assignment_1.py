class BankAccount:
    _AccountCount = 0

    def __init__(self, lastName, firstName, taxIDNumber, checkingBalance, \
                 savingsBalance, savingsInterestRate):
        BankAccount._AccountCount += 1
        self.accountNumber = "A-00" + str(BankAccount._AccountCount)
        self.lastName = lastName
        self.firstName = firstName
        self.taxIDNumber = taxIDNumber
        self.savingsBalance = savingsBalance
        self.checkingBalance = checkingBalance
        self.savingsInterestRate = savingsInterestRate

        if checkingBalance > 1000.00 and savingsBalance > 500.00:
            self.minCheckingBalance = 0.25 * checkingBalance
            self.maxCheckingWithdrawal = 0.4 * checkingBalance
            self.minSavingBalance = 0.55 * savingsBalance
            self.maxSavingWithdrawal = 0.2 * savingsBalance
            print(f"Account {self.accountNumber} HAS BEEN CREATED")
        else:
            print(f"Account {self.accountNumber} IS PENDING ADDITIONAL FUNDS")
            self.minCheckingBalance = 0.00
            self.maxCheckingWithdrawal = 0.00
            self.minSavingBalance = 0.00
            self.maxSavingWithdrawal = 0.00

    def displayAccountInfo(self):
        print(f"Account Number: {self.accountNumber}\n" \
              f"Name on Account: {self.firstName} {self.lastName}\n" \
              f"Tax ID Number: {self.taxIDNumber}\n" \
              "-----------------BALANCES----------------\n" \
              f"            Checking: ${self.checkingBalance}\n" \
              f"            Savings: ${self.savingsBalance}\n" \
              "-----------------ALLOWANCES______________\n" \
              f"Minimum Checking Balance: ${self.minCheckingBalance}\n" \
              f"Maximum Checking Withdrawal: ${self.maxCheckingWithdrawal}\n" \
              f"Minimum Savings Balance: ${self.minSavingBalance}\n" \
              f"Maximum Savings Withdrawal: ${self.maxSavingWithdrawal}")

    def depositToChecking(self, d):
        self.checkingBalance += d
        print(f"${d} deposited to Checking")
        return True

    def depositToSavings(self, d):
        self.savingsBalance += d
        print(f"${d} deposited to Savings")
        return True

    def withdrawFromChecking(self, d):
        if self.checkingBalance > self.checkingBalance - d > self.minCheckingBalance:
            self.checkingBalance -= d
            print(f"${d} withdrawn from Checking")
            return True
        else:
            print("Withdraw cannot be made")
            return False

    def withdrawFromSavings(self, d):
        if self.savingsBalance > self.savingsBalance - d > self.minSavingBalance:
            self.savingsBalance -= d
            print(f"${d} withdrawn from Savings")
            return True
        else:
            print("Withdraw cannot be made")
            return False


B1 = BankAccount("Johnson", "Bobby", 123456, 2390.00, 3400.00, 0.02)
B2 = BankAccount("Thomas", "Richard", 654888, 5360.00, 5400.00, 0.025)
B3 = BankAccount("Turner", "James", 622898, 360.00, 5400.00, 0.021)

B1.depositToChecking(100.32)
B1.depositToSavings(2000.00)
B1.withdrawFromChecking(90.00)
B1.displayAccountInfo()

B2.depositToChecking(1230.02)
B2.depositToSavings(1000.00)
B2.withdrawFromSavings(765.00)
B2.displayAccountInfo()

B3.displayAccountInfo()
