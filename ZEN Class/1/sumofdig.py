n=int(input())
s=0
m=0
while(n>0):
    m=n%10
    s=s+m
    n=n//10
print(s)
