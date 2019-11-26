n=int(input())
count=0
for i in range(1,n):
    if(n%i==0):
        count+=1
print(count)
if(count>1):
    print("not prime")
else:
    print("prime")
    
    
