import random
randNumber = random.randint(1,100)
UserGuess = None
guesses = 0

while(UserGuess != randNumber):
    UserGuess = int(input("Enter your guesses: "))
    guesses +=1
    if(UserGuess==randNumber):
        print("You gusses it right!")
    else:
        if(UserGuess>randNumber):
            print("You guessed it wrong! Enter a smaller number")
        else:
            print("You guessed it wrong! Enter a larger number")
    
    
print(f"You guesses the number in {guesses} guesses")

with open("hiscore.txt", "r") as f:
    hiscore = int(f.read())

if(guesses<hiscore):
    print("You have just broken the high score!")
    with open("hiscore.txt", "w") as f:
        f.write(str(guesses))