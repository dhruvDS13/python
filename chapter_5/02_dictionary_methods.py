myDict = {
    "Fast": "In a Quick Manner",
    "Dhruv": "A coder",
    "Marks": [1,2,6],
    "anotherdict": {'dhruv':'Engineer'},
    1:2
}

# print(myDict.keys())
# print(type(myDict.keys()))

# print(list(myDict.keys())) # print the keys of the Dictionary 
# print(myDict.values()) # print the values of the Dictionary
# print(myDict.items()) # print the (key,value) for all content of the Dictionary

print(myDict)
updateDict={
"Aryan":"friend",
"Rahul":"friend",
"Arpan":"friend",
"Jay":"A dancer"
}
myDict.update(updateDict) # updates the dictionary by adding key-value paris from updateDict 
print(myDict)

print(myDict.get("Jay")) # print value associated with key "Jay"
print(myDict["Jay"]) # print value associated with key "Jay"

# The key difference between .get and [] syntax in Dictionary
print(myDict.get("Jay2")) # Return none as Ja2 is not present in the dictionary
print(myDict["Jay2"]) # throws an error Jay2 is not present in the dictionary