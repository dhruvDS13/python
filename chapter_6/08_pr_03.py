text = input("Enter the text: ")

if ("make a lot of money" in text):
    spam = True
elif ("buy now" in text):
    spam = True
elif ("click this" in text):
    spam = True
elif ("subscribe this" in text):
    spam = True
else:
    spam = False

if(spam):
    print("This Text is spam ")
else:
    print("This Text is not spam ")
