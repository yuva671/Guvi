n=int(input())
c=input().split()
a=list()
for i in range(0,n,2):
    c[i],c[i+1]=c[i+1],c[i]
    a+=[c[i],c[i+1]]
print(a)
