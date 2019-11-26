n=input()
a=list(n)
l=len(n)-1
c=a[0]
a[0]=a[l]
a[l]=c
print("".join(map(str,a)))


    
