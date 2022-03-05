string1=input("\nEnter a string\n")
string1=string1.casefold()
vowels="aeiou"
data={}.fromkeys(vowels,0)
for ch in string1:
    if ch in vowels:
        data[ch]+=1
for vowel in data:
    print(vowel,"=>",data[vowel])