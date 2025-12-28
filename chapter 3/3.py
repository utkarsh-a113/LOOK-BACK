a=input("enter the string: ")
if "  " in a:
    print("Double spaces were used here") 
else:
    print("No double spaces were used here")
print("in another block")
print(a.find("  "))
print(a.replace("  ","//"))
