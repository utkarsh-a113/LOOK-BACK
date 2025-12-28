# d={"namaste":"hello",
# "dog":"cat",
# "cat":"billi",
# "home":"ghar"
# }

# x=input("enter the key word: ")
# z=d.get(x)
# print(z)
# Hindi to English dictionary
hindi_dict = {
    "pustak": "book",
    "kutta": "dog",
    "billi": "cat",
    "ghar": "house",
    "pani": "water"
}

print("Hindi to English Dictionary")
print("Available words:", ", ".join(hindi_dict.keys()))

# Ask user to enter a Hindi word
word = input("Enter a Hindi word to look up: ")

# Lookup the word in dictionary
translation = hindi_dict.get(word)

if translation:
    print(f"The English translation of '{word}' is '{translation}'")
else:
    print(f"Sorry, '{word}' is not in the dictionary.")
