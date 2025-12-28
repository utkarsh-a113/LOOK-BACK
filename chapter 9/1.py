# f=open("poems.txt","r")
# f = open("poems.txt", "r")
f = open(r"C:\Users\lenovo\Desktop\python2\chapter 9\poems.txt", "r")

text=f.read()
if ("twinkle" in text):
    print("yep")
print(f"the original text is {text}")