from graphics.rectangle import*
from graphics.circle import*
from graphics.td_graphics.cuboid import*
from graphics.td_graphics.sphere import*
print("Select Operation. \n 1.Rectangle\n 2.Circle\n 3.Sphere\n 4.Cuboid\n 5.Exit")
while True:
    choice=input("\nEnter The choice:")
    if choice in ('1','2','3','4','5'):
        if choice=='1':
            l=int(input("\nEnter the Length: "))
            b=int(input("\nEnter the Breadth"))
            print("\nArea of the Rectangle is : ",rectarea(l,b))
            print("\nPerimeter of The Rectangle is : ",rectperi(l,b))
        if choice=='2':
            r=int(input("\nEnter the Radius: "))
            print("\nArea of the Circle is : ",circlearea(r))
            print("\nPerimeter of The Circle is : ",circleperi(r))
        if choice=='3':
            sr=int(input("\nEnter the Radius: "))
            print("\nArea of the Sphere is : ",spherearea(sr))
            print("\nPerimeter of The Sphere is : ",sphereperi(sr))
        if choice=='4':
            cl=int(input("\nEnter the Length: "))
            w=int(input("\nEnter the Width"))
            h=int(input("\nEnter the Height"))
            print("\nArea of the Cuboid is : ",cuboidarea(cl,w,h))
            print("\nPerimeter of The Cuboid is : ",cuboidperi(cl,w,h))
        if choice=='5':
            exit(0)
        else:
            print("\nInvalid Input")