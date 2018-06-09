# Simulate the Banking system

# Saving Account class
from abc import ABCMeta, abstractmethod
from random import randint


class bankAccount(metaclass = ABCMeta):
    @abstractmethod
    def createSavingsAccount():
        return 0

    @abstractmethod
    def accountAuthenticate():
        return 0

    @abstractmethod
    def withdrawAmount():
        return 0

    @abstractmethod
    def depositAmount():
        return 0

    @abstractmethod
    def displayBalanceAmount():
        return 0





class SavingsAccount:
    def __init__(self):
        self.savingsAccounts = dict()

    # creating a new account
    def createSavingsAccount(self, firstName, lastName, intialDepositAmount):
        self.accountNumber = randint(100000, 999999)
        self.savingsAccounts[self.accountNumber] = [firstName, lastName, intialDepositAmount]
        print("Account created successfully")
        print("Your Account Number is ", self.accountNumber)

    # verify the account is valid or not
    def accountAuthenticate(self, lastName, accountNumber):
        if accountNumber in self.savingsAccounts.keys():
            if self.savingsAccounts[accountNumber][1] == lastName:
                print("Valid Account and Authentication Successful")
                self.accountNumber = accountNumber
                return True
            else:
                print("Account Number matches but your lastName doest match with account. Please try again")
                return False
        else:
            print("Entered Account is not valid")
            return False
    # withdraw and update the balance
    def withdrawAmount(self, withdrawAmount):
        if withdrawAmount > self.savingsAccounts[self.accountNumber][2]:
            print("Insufficient funds")
        else:
            self.savingsAccounts[self.accountNumber][2] -= withdrawAmount
            print("Your Withdraw Amount tansaction is successful")
            self.displayBalanceAmount()
    # Deposit and update the balance
    def depositAmount(self, depositAmount):
        self.savingsAccounts[self.accountNumber][2] += depositAmount
        print("Your balance is updated successfully")
        self.displayBalanceAmount()
    # display the balance
    def displayBalanceAmount(self):
        print("Available Balance: ", self.savingsAccounts[self.accountNumber][2])

savingsAccount = SavingsAccount()
while True:
    print("welcome to SUPERDUPER FANCY BANK!!!")
    print("Please check the below options to move forward: ")
    print("Option A: Enter 1 to create an account")
    print("Option B: Enter 2 to access an existing account")
    print("Option C: Enter 3 to exit")
    userInput = int(input())
    if userInput == 1:
        print("Enter your first name: ")
        firstName = input()
        print("Enter your last name: ")
        lastname = input()
        print("Enter the amount you want to deposit: ")
        depositAmount = int(input())
        savingsAccount.createSavingsAccount(firstName, lastName, depositAmount)
    elif userInput == 2:
        print("Enter your last name: ")
        lastName = input()
        print("Enter your account number: ")
        accountNumber = int(input())
        accountValidation = savingsAccount.accountAuthenticate(lastName, accountNumber)
        if accountValidation is True:
            while True:
                print("Option A: Enter 1 to withdraw amount")
                print("Option B: Enter 2 to deposit amount")
                print("Option C: Enter 3 to check you available balance")
                print("Option D: Enter 4 to main menu")
                print("Option E: Enter 5 to exit")
                userInput = int(input())
                if userInput == 1:
                    print("Enter the amount to withdraw")
                    withdrawAmount = int(input())
                    savingsAccount.withdrawAmount(withdrawAmount)
                    print("Thank You for Banking with us")
                elif userInput == 2:
                    print("Enter the amount to deposit")
                    depositAmount = int(input())
                    savingsAccount.depositAmount(depositAmount)
                    print("Thank You for Banking with us")
                elif userInput == 3:
                    savingsAccount.displayBalanceAmount()
                    print("Thank You for Banking with us")
                elif userInput == 4:
                    break
                elif userInput == 5:
                    print("Thank You for Banking with us")
                    quit()
                else:
                    print("Invalid choice. Please check the options Once again")
        else:
            print("There is no existing account matching the input: Please check the details")
            print("Do you want to retry again :")
            print("Option A: Enter 1 to continue: ")
            print("Option B: Enter 2 to quit")
            userInput = int(input())
            if userInput == 1:
                print("Main Menu")
            elif userInput == 2:
                print("Thank You for Banking with us")
                quit()
            else:
                print("Invalid input:")
                quit()
    elif userInput == 3:
        print("Thank You for Banking with us")
        quit()
    else:
        print("Invalid input choice. Please check the options once again: ")






















    
    
