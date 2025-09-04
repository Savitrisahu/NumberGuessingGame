import random

correctNum = random.randint(1, 100)
guessNum = int(input("Enter number for guessing: "))
attempt = 0
while guessNum != correctNum:
    if guessNum < correctNum:
        print("The number is bigger.\nTry again.")
    elif guessNum > correctNum:
        print("The number is smaller.\nTry again.")
    
    guessNum = int(input("Enter number for guessing: "))
    attempt+= 1

print(f"YOU WIN 🎉\nCorrect number is {correctNum} and your guessed number is {guessNum}, you make {attempt} attempts")
