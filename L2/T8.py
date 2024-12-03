firstname = input("What is your first name?")
print("Hello", firstname)
surname = input("What is your surname?")
print("Your surname is ", surname)

surname_f3 = surname[:3].lower()
firstname_f1 = firstname[:1].lower()
surname_length = str(len(surname))

username = surname_f3 + firstname_f1 + surname_length
print(username)