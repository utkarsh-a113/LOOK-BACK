def remove_word(l, remove):
    clean = [w.strip() for w in l]
    if remove.strip() in clean:
        clean.remove(remove.strip())  
    return clean
words = [" apple ", "banana", " orange ", "grape "]
result = remove_word(words, "orange")
print("Original list:", words)
print("After removing:", result)
