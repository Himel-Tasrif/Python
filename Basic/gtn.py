# Guess The Number:

from random import randint
for x in range(1,6):
    guessNumber = int(input("Enter a number between 1-5: "))
    randomNumber = randint(1,5)

    if guessNumber == randomNumber:
        print("You are correct !!!")
    else:
        print("You are not correct !!")
        print("The correct number is: ",randomNumber)