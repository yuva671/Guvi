list1=input().split()
d1={}
for items in list1:
    if items in d1:
        print(items,d[items])
        d1[items]+=1
        print(d1[items])
        print(d1.items)
        break
    else:
        d1[items]=1
        print(d1[items])
        print(items)
        break

for key, value in d1.items(): 
        print (key, value) 
