
myDictionary = {
    "One": "Yuvraj",
    "Two": "Singh",
    "Three": 8900,
    "Four": 303
}

print(myDictionary)
print(myDictionary["One"])
print(myDictionary.keys())  # They are just displayed in the form of a list, and not stored in the form of a list
print(myDictionary.values())

myList = list(myDictionary.keys())  # To convert them into a list
print(myList[1])