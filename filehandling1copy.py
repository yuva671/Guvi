import os
source=r'C:\Users\yuva0\Desktop\source'
destination=r'C:\Users\yuva0\Desktop\destination'
files=os.listdir(source)
for f in files:
    print(f)
    file=open(source+'\\'+f,'rb')
    var1=file.read()
    file.close()
    Newfile=open(destination+'\\'+f,'wb')
    Newfile.write(var1)
    Newfile.close()
