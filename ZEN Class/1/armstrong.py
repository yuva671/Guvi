num = int(input())  

for i in range(0,num+1):
   s = 0  
   temp = num
   order=len(str(abs(num)))
   while(temp > 0):  
      digit = temp % 10  
      s += digit ** order  
      temp //= 10  
   if(num == s):  
      print(num)  

