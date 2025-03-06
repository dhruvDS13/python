def remove_and_split(string, word):
    newStr = string.replace(word, "")
    return newStr.strip()

this = "    Dhruv is a Good boy    "
n = remove_and_split(this, "Dhruv")
print(n)
# print(this)
# print(this.strip())