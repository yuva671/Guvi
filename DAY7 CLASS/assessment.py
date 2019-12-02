list1=input().split()
list2=input().split()

a=list1[len(list1)-1]
for i in range(len(list1)-1,-1,-1):
    if(list2[i]==a):
        print(i-1)
print(list1)

