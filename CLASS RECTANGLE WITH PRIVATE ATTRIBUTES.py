class rectangle():
    length=None
    width=None
    def __init__(self):
        self.length=int(input("\nEnter the length: "))
        self.width=int(input("\nEnter the Width: "))
    def area(self):
        return(self.length*self.width)
r1=rectangle()
r2=rectangle()
print("\nArea of Rectangle : ",r1.area())
print("\nArea of Rectangle : ",r2.area())
if r1.area()>r2.area():
    print("\nArea 1 is Greater ")
else:
    print("\nArea 2 is Greater ")