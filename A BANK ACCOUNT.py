class bank:
    def __init__(self):
        self.accno=int(input("\nEnter Account number: "))
        self.name=input("\nEnter the Account Holder Name: ")
        self.acctype=input("\nEnter the Account Type: ")
        self.balance=int(input("\nEnter the Balance: "))
    def deposit(self):
        amount=int(input("\nEnter The Amount to Be deposited: "))
        self.balance+=amount
        print("\nThe Acoount balance is : ",self.balance)
    def withdraw(self):
        amount=int(input("\nEnter the amount to withdraw: "))
        if (self.balance>=amount):
            self.balance-=amount
            print("\nYou Have Withdrawn Rs.",amount)
        else:
            print("\nYou have Insufficient Balance")
    def display(self):
        print("\nNet Available Balance is: ",self.balance)
a=bank()
a.deposit()
a.withdraw()
a.display()


