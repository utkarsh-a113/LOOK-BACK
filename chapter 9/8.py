with open(r"C:\Users\Lenovo\Desktop\python2\chapter 9\this.txt") as f:
    content=f.read()
with open("this_copy.txt","w") as f:
    f.write(content)