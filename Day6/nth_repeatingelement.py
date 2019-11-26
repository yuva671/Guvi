l=input().split()
count_list=[]
value_list=[]
count=1
for i in range(0,len(l)):
    for j in range(i+1,len(l)):
        if(l[i]==l[j]):
            count=count+1
    count_list.append(count)
    value_list.append(l[i])
    count=1
        
        

print(value_list)
print(count_list)







    
