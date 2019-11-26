n=int(input())
a=[]
while(n>0):
    temp=n%10
    a.append(temp)
    n=n//10
print(a)
v_list=[]
c_list=[]
for i in range(0,len(a)):
    v_list.append(a[i])
for i in v_list:
    c_list.append(a.count(i))
print(v_list)
print(c_list)
            
    
