n=int(input())
c= input().split()
a = list()
for i in range(0,n,2):
    c[i]=c[i]+c[n]
    c[n]=c[i]-c[n]
    c[i]=c[i]-c[n]
print(c)

