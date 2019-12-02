list1=[8,4,9,8,10,5,13,4]
if (list1[1] > list1[0] and list1[1] > list1[2]):
    for i in range(1, len(list1)-1):
    
        
        if (list1[i] > list1[i - 1] and list1[i] > list1[i + 1]): 
            print("True")
            break
          
        else: 
            print("False")
            break
else if(list1[1] < list1[0] and list1[1] < list1[2]) : 
    for i in range(1, len(list1)-1):
        if (list1[i] < list1[i - 1] and list1[i] < list1[i + 1]): 
            print("True")
            break
          
        else: 
            print("False")
            break
    
