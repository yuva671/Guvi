l=input().split()
value_list=[]
count_list=[]
for i in range(0,len(l)):
    if l[i] not in value_list:
        value_list.append(l[i])
for i in value_list:
    count_list.append(l.count(i))
print(value_list)
print(count_list)

n=int(input())
list1=[]
for i in range(0,len(value_list)):
    if(count_list[i]>1):
        
            list1.append(value_list[i])
print(list1)
print(list1[n-1])

    
    
