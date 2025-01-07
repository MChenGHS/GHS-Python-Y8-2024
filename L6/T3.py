import random
random_number = random.randint(1, 10)
guess_number = int(input("Guess a number: "))

while guess_number != random_number:
    guess_number = int(input("That wasn't what I have. Guess a number: "))
print("Good job!")