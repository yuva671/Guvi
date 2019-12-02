s=input()
list1=list(s)
print(list1)
vowels=['a','e','i','o','u']
consonant=0
count=0
for i in range(0,len(list1)):
    if list1[i] in vowels:
        count=count+1
    else:
        consonant=consonant+1
print(count)
print(consonant)

