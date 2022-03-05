a=input("Enter the first string ")
b=input("Enter the Second String ")
x=a[0:2]
a=a.replace(a[0:2],b[0:2])
b=b.replace(b[0:2],x)
print("After Swaping")
print(a,b)