filenames=["1.txt","2.txt","3.txt"]
for file in filenames:
    try:
        with open(file,"r") as f:
            print(f"Content of {file}:")
            print(f.read())
            print("-"*30)
    except FileNotFoundError:
        print(f"file'{file}' not found.")