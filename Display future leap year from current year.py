a=2022
print("\nEnter the last year\n")
b=int(input())
print("\nList of Leap Year\n")
for c in range(a,b):
    if(0==c%4)and(0!=c%100)or(0==c%400):
        print(c)
