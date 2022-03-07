from secrets import choice


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
print("Welcome to Bank")
a=bank()
while True:
   print("Select the option \n 1.Account Details\n 2.Deposit money \n3.Withdraw Money \n 4.Exit")
   chose=int(input())
   if chose==2:
    a.deposit()
   if chose==3:
    a.withdraw()
   if chose==1:
    a.display()
   if chose==4:
    exit()


