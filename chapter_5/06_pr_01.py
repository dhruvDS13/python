myDict = {
    "pankha":"fan",
    "dawai":"medicine",
    "talwar":"sword",
    "akhbar":"newspaper",
    "toliya":"towel",
    "janwar":"animal",
    "chidya":"bird"
}
print("Options are",myDict.keys())
a = input("Enter the Hindi word:\n")

# print("The meaning of the word is:", myDict[a])
print("The meaning of the word is:", myDict.get(a))