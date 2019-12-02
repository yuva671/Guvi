string="Abcdef"
def upper(val):
    for i in range(0,len(string)):
        if(string[i]>='a' and string[i]<='z'):
            print("first")
            return(False)
    return(True)
if(upper(string)):
    print("true")
else:
    print("false")
