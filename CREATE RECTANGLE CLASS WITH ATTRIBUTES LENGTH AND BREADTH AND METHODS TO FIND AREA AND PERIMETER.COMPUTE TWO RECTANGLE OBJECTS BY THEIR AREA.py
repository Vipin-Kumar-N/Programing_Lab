class rectangle():
    def __init__(self):
        self.length=int(input("Enter the Length : "))
        self.breadth=int(input("Enter the Breadth : "))
    def area(self):
        return(self.length*self.breadth)
    def perimeter(self):
        return(2*(self.length+self.breadth))
r1=rectangle()
r2=rectangle()
print("Area of Rectangle= ",r1.area())
print("Perimeter of Rectangle= ",r1.perimeter())
print("Area of Rectangle= ",r2.area())
print("Perimeter of Rectangle= ",r2.perimeter())
if(r1.area()==r2.area()):
    print("\nAreas Are the Same ")
else:
    print("\nDifferent")