num=int(input("Enter the Number "))
for row in range(1,num+1):
    for col in range(1,row+1):
        print(row*col,end=" ")
    print()