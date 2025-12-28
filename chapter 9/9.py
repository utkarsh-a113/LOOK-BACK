with open(r"C:\Users\Lenovo\Desktop\python2\chapter 9\file1.txt") as f:
    content1=f.read()
with open(r"C:\Users\Lenovo\Desktop\python2\chapter 9\file2.txt") as f:
    content2=f.read()
if(content1==content2):
    print("print yes these files are identical")
else:
        print("print yes these files are not identical")