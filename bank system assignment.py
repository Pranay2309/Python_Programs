class BankSystem:
    def __init__(self):
        self.bal=0

    def deposit(self):
        name=input("Enter your name :")
        print("\nWelcome ",name)
        amt=int(input("\nEnter the amount to be deposited :"))
        self.bal=self.bal+amt
        print("Amount deposited :",amt)

    def withdrawal(self):
        amt=int(input("Enter amount to be withdrawn :"))
        if self.bal>amt:
            self.bal=self.bal-amt
            print("Amount withdrawn :",amt)
        else:
            print("Insufficient Balance :")

    def display(self):
        print("Available Balance :",self.bal)
ob1=BankSystem()
ob1.deposit()
ob1.withdrawal()
ob1.display()
