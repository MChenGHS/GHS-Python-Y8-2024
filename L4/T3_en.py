number = int(input("How many crossiants do you want? "))

if number <= 5:
    price = number * 3
else:
    price = number * 2

print("The total price is ", price, "euros.")