l=[1,2,3,4,5,6,7,8]
for i,value in enumerate(l,start=1):
    if i in [3,5,7]:
        print(f"{i}rd/ th element={value}")


# enumerate(iterable, start=0)
# iterable: list, tuple, string, etc.
# start: the starting index (default = 0).