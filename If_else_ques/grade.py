# Calculate the grade of a student based on their score.

i = int(input("Enter the student's score: "))

if i >= 90:
    grade = 'A'
elif i >= 80:
    grade = 'B'
elif i >= 70:
    grade = 'C'
elif i >= 60:
    grade = 'D'
elif i >= 40:
    grade = 'E'
else:
    grade = 'F'

print("The student's grade is:", grade)