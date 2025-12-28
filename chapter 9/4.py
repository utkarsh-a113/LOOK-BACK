word="donkey"
with open(f"chapter 9\send.txt","r") as f:
    text=f.read()
newtext=text.replace(word,"3333")
with open(f"chapter 9\send.txt","w") as f:
    f.write(newtext)