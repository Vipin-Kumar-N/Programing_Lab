import string


string=input("Enter the String : ")
start=string[0]
end=string[-1]
swapped=end+string[1:-1]+start
print(swapped)