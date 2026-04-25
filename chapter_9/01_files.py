# Use open function to read the content of a file!
# f = open('sample.txt','r')
f = open('sample.txt','r') # by default read karega
data = f.read()
print(data)
f.close()
# cd = change directory (cd chapter_9)
# cd.. for previous directory