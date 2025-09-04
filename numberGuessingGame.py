import random

correctNum = random.randint(1, 100)
attempt = 0

while True:
    try:
        guessNum = int(input("Enter number for guessing between (1 – 100): "))
        if guessNum < 1 or guessNum > 100:
            print("Please enter a number between 1 and 100.\n")
            continue

        attempt += 1

        if guessNum == correctNum:
            print(f"YOU WIN \nCorrect number is {correctNum} and you guessed it in {attempt} attempts.")
            break
        elif guessNum < correctNum:
            print("The number is bigger.\nTry again.\n")
        else:
            print("The number is smaller.\nTry again.\n")

    except ValueError:
        print("Invalid input! Please enter a valid integer.\n")

