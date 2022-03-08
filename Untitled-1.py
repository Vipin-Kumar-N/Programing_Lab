""" a=input("Enter List1: ")
a=a.split(" ")
a=list(map(int,a))
print("\n",len(a),"\n",a)
b=0
for i in range (0,len(a)):
    b+=a[i]
print(b) """

"""dict1={}
a=int(input("Enter no of keys"))
for i in range(a):
    key=input("Enter Key" )
    value=input("Enter the value")
    dict1[key]=value
print(dict1)"""

"""a=input("Enter a string: ")
x=" "
x+=a[0]
for i in range(1,len(a)):
    if a[i]==a[0]:
        x+='$'
    else:
        x+=a[i]
print(x)"""

"""a=input("Enter the Sentence : ")
a=a.split(" ")
s={}
for i in a:
    if i in s:
        s[i]+=1
    else:
        s[i]=1
print(s)"""

"""num1=int(input("Enter the number"))
s=0
temp=num1
while temp>0:
    digit=temp%10
    s+=digit**3
    temp=temp//10
if (num1==s):
    print("Its Amstrong")
else:
    print("Its Not")"""

"""a=int(input("Enter the Step :"))
for i in range(1,a+1):
    print()
    for j in range(1,i+1):
        print(i*j,end=" ")"""

"""
d1={8 : 'Name',6:'four',9:'eight',0:'Zero',4:'govt'}
print('the {0} is the dictionary'.format(d1))
l1=list(d1.items())
l1.sort()
print(l1)
d2=dict(l1)
print(d2)
l2=list(d2.items())
l2.sort(reverse=True)
d3=dict(l2)
print(d3)
"""

