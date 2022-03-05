list1=[11,22,33,44,55]
print("list: ",list1)
for i in list1 :
    if(i%2==0):
        list1.remove(i)
print("List after removing Even numbers : ",list1)