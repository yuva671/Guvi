n=int(input())
k=int(input())
n1=list()
for i in range(0,(n+1)):
    n1.append(int(input()))
    print(n1)
    if k not in n1:
        print("no")
    else:
        print("yes")


