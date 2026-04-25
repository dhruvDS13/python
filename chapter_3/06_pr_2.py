letter = '''Dear <|NAME|>,
Greetings form ABC coding house. I am happy to tell you about your selection
You are selected!
Have a great day ahead!
Thanks and regrads,
Bill
Date: <|DATE|>
'''
name = input("Enter yout Name:\n")
date = input("Enter Date:\n")
letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|DATE|>", date)
print(letter)