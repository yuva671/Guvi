n=int(input())
alist=list()
count=0
alist1=list()
for i in range(1,n):
    b=int(input())
    alist.append(b)
print(alist)
for i in range(0, len(alist)):
    for j in range(i+1, len(alist)):
        if(alist[i] == alist[j]): 
            alist1=alist[j] 
            print(alist1)
if(alist1==[]):
    print('-1')
            