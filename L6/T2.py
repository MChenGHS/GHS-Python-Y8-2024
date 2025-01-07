correct_password = "sm39ps"
input_password = input("What's the password? ")
while input_password != correct_password:
    print("Incorrect")
    input_password = input("Let's try again. What's the password? ")
print("Correct")