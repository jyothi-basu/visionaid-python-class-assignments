import random

#a small number guessing game.
print("Welcome to my small number guessing game!")
target= random.randint(1, 100)
attempts= 0
while True: 
    guess= int(input("Please guess a number between 1 to 100: "))
    attempts += 1
    if guess > target:
        print("Your number is too high, Please try again!")
    elif guess < target:
        print("Your number is Too low, please try again!")
    else:
        print("Your guess is Correct! congratulations you got this in",attempts,"attempts")
        break