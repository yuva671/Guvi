fruits=["apple","banana","grapes"]
def search(val):
    for i in fruits:
        if(i==val):
            return(True)
        else:
            return(False)
if(search("grapes")):
    print("true")
else:
    print("false")
