string=input()
alpha=0
num=0
special=0
for i in range(0,len(string)):
    if(string[i]>='a' and string[i]<='z'):
        alpha=alpha+1
    elif(string[i]>='A' and string[i]<='Z'):
        alpha=alpha+1
    elif(string[i]>='0'and string[i]<='9'):
        num=num+1
    else:
        special=special+1
print("alpha", alpha)
print("num=", num)
print("special=", special)
    

