import os
import shutil
main=r'C:\Users\yuva0\Desktop\Dummy'
dirs=r'C:\Users\yuva0\Desktop\temp'
for root,subdirs,files in os.walk(dirs):
    print("root",root)
    print("subdirs",subdirs)
    print("files",files)
    for file in files:
        path=os.path.join(root,file)
        shutil.move(path,main)
