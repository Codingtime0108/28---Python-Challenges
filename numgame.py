import random

print("Welcome to 'Guess the Number'!")
print("I'm thinking of a number between 1 and 20.")
print("Can you guess what it is?")

number_to_guess = random.randint(1, 20)

if number_to_guess %2 == 0:
        print("This number is even!")
else:
        print("This number is odd!")

tries = 0

while True:
    user_guess = int(input("Tell me what u think:"))
    if number_to_guess > user_guess:
        print("Think of something higher")
        tries = tries+1
    elif number_to_guess < user_guess:
        print("Think of something lower")
        tries = tries+1
    else:
        print("Got it!!!!")
        tries = tries+1
        print("You got it in",tries,"gueses")
        break