num=int(input("Enter the Value : "))
total=0
for i in range(0,num):
    total+=int(str(num)+i*str(num))
print(total)