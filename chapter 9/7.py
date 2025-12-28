line=1
with open(r"C:\Users\Lenovo\Desktop\python2\chapter 9\log.txt") as f:
    lines=f.readline()
lineno=1
for line in lines:
    if("python" in line):
        print(f"yes python is present in {lineno}")
        break 
    lineno+=1

else:
    print("no python is not present")
