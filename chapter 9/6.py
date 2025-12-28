# Write a program to mine a log file and find out whether it contains ‘python’
with open(r"C:\Users\Lenovo\Desktop\python2\chapter 9\log.txt") as f:
    content=f.read()
if("python" in content):
    print("yes python is present")
else:
    print("no python is not present")
