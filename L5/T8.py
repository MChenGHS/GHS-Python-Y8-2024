score = int(input("What is the score received? "))
grade = ""
if score >= 75:
    grade = "A"
elif score >= 60:
    grade = "B"
elif score >= 35:
    grade = "C"
else:
    grade = "D"
print(grade)