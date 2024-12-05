score = int(input("Enter the score: "))

if score >= 80:
    grade = "M"
elif score >= 60:
    grade = "S"
elif score >= 35:
    grade = "D"
else:
    grade = "E"

print("Grade:", grade)