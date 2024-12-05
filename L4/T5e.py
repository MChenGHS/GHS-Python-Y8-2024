score = int(input("Enter the score: "))

if score >= 0 and score <= 100:
    if score >= 80:
        grade = "M"
    elif score >= 60:
        grade = "S"
    elif score >= 35:
        grade = "D"
    else:
        grade = "E"
    print("Grade:", grade)
else:
    print("Invalid score. Please enter a score between 0 and 100.")