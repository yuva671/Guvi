list1=input().split()
for i in range(0,3):
    temp=list1[0]
    for i in range(0,len(list1)-1):
        list1[i]=list1[i+1]
    list1[len(list1)-1]=temp
