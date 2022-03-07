""""
sy=int(input("Enter the start year"))
ey=int(input("Enter the end year"))
for y in range(sy,ey+1):
    if y%4==0 and y%100!=0 or y%400==0:
        print(y)

"""
"""
lst=[-55,61,32,-56,-44,200,-101]
posi=list(filter(lambda x : x>0,lst))
print(posi)

"""

"""

lst=[-55,61,32,-56,-44,200,-101]
sq=list(n**2 for n in lst)
print(sq)

"""
"""

st=input("Enter a string")
v=['a','e','i','o','u']
d={}.fromkeys(v,0)
for a in st:
    if a in v:
        d[a]+=1
print(d)
    
"""

"""

a=input("Enter a word ")
for b in a:
    print(ord(b),end=" ")

"""

"""

i=input("Enter a string ")
i=i.split(" ")
d={}.fromkeys(i,0)
print(i)
for a in i:
    d[a]+=1
print(d)

"""

"""

def conv(a):
    n=""
    for x in a:
        n+=x
    return n
s=['ammu','ponnu','anju','achu','pooja']
st=list(conv(s))
print("no .of a is")
print(st.count('a'))

"""

"""

st=input("string ")
print(st[0]+st[1:].replace(st[0],'$'))

"""

"""
st=input("String")
st2=st[-1]+st[1:-1]+st[0]
print(st2)

"""

"""

clor=input("Enter the colors :")
n=clor.split(" ")
print(n[0],n[-1])

"""

"""

ina=int(input("Enter the value "))
total=0
for i in range(0,ina):
    total+=int(str(ina)+i*str(ina))
print(total)

"""

"""

y={'carl':40,'alan':2,'bob':1,'danny':3}
l=list(y.items())
l.sort()
d=dict(l)
print(d)
l.sort(reverse=True)
d=dict(l)
print(d)

"""

"""

a=input("String1 : ")
b=input("String2 : ")
x=a[0:2]
c=a.replace(a[0:2],b[0:2])+" "+b.replace(b[0:2],x)
print(c)

"""

"""

lis=[22,3,45,69,45,11,232,4556,124,125,1110]
lis2=[]
for i in lis:
    if i%2==0:
        lis2.append(i)
print(lis2)

"""

"""

step=int(input("Enter the step"))
for i in range(1,step+1):
    print()
    for j in range(1,i+1):
        print(i*j,end=" ")

"""

"""

string1=input("Enter string ")
d={}
for i in string1:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)

"""

"""

str1=input("Entr the String ")
if str1.endswith('ing'):
    str1+='ly'
elif len(str1)>=3:
    str1+='ing'
print(str1)

"""

"""

num1=int(input("Enter number "))
for i in range (1,num1):
    if (num1%i==0):
        print(i)

"""

"""
class React1():
    def __init__(self):
        self.l=int(input("Lenght"))
        self.b=int(input("L"))
    def area(self):
        return self.l*self.b
    def peri(self):
        return 2*(self.l+self.b)
r1=React1()
r2=React1()
print(r1.area())
print(r2.peri())

"""

"""

with open("Text.txt") as f:
    content=f.readlines()
    li=[x.strip() for x in content]
    print(li)

"""

"""
f1=open("text1.txt",'r')
f2=open("text2.txt",'r')
content=f1.readlines()
type(content)
for i in range(0,len(content)):
    if (i%2==0):
        f2.write(content[i])
    else:
        pass
f2.close()
f2=open("Text2.txt")
content1=f2.readlines()
print(content1)
f1.close()
f2.close()
"""

"""
import csv
with open("file.csv") as csvfile:
    data=csv.reader(csvfile,delimiter=" ",quotechar='|')
    for row in data:
        print(','.join(row))

"""

"""

import csv
with open("file.csv") as csvfile:
    data=csv.reader(csvfile)
    for line in data:
        print(line[2])

"""

"""

import csv
with open("file.csv") as csvfile:
    fieldnames=['Name','Department','Birthday']
    content=csv.DictWriter(outf,fieldnames=fieldnames)
    content.writeheader()
    content.writerow({'Name':'Amy','Department': 'IT','Birthday':'November'})

"""

"""

str1=input("Enter the string : ")
str2=input("Substring to be found : ")
substr1=str1.count(str2)
print(substr1)

"""