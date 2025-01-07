import random
lives = 3
random_number = random.randint(1, 10)
guess_number = int(input("Guess a number: "))

while guess_number != random_number:
    lives = lives - 1

    if lives == 0:
        break

    guess_number = int(input("That wasn't what I have. Guess a number: "))

if lives != 0:
    print("Good job!")
else:
    print("Sorry, you've run out of chances")