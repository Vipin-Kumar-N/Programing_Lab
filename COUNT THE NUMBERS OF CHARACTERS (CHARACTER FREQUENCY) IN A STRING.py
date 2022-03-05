test1=input("Enter a String : ")
freq={}
for i in test1:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
print("Count of all Characters in "+test1+"is : \n"+str(freq))
