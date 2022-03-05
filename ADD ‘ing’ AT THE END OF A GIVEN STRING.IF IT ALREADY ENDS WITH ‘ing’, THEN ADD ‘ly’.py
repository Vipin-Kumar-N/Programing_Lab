import string


string=input("Enter the string : ")
if string.endswith('ing'):
    string+='ily'
elif(string)>=3:
    string+='ing'
print(string)