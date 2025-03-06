# creating an empty set
b = set()
print(type(b))

# Adding value in empty set
b.add(4)
b.add(5)
b.add(5)
b.add(5) # Adding a value repeatedly does not change a set
# b.add([4,5,6]) # TypeError: unhashable type: 'list'
b.add((4,5,6)) # add tuple in set

## Accessing Elements
# b.add({4:5}) # cannot ass list or dictionary to set
print(b)

## Length of the set
print(len(b)) # print the length of this sets

## Removal of an Item
b.remove(5)
# b.remove(15) #throw an error while trying to remove 15(which is not present in the set)
print(b)

## Remove an any arbritry Elements
# print(b.pop())
# print(b)

## Clear set
# b.clear()
# print(b)

b.union({2,7,8})
print(b)