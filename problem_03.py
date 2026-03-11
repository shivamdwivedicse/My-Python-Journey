print("Welcome to the Student Grade Evaluator 🎓")

sub1 = int(input("Enter marks of Subject 1: "))
sub2 = int(input("Enter marks of Subject 2: "))
sub3 = int(input("Enter marks of Subject 3: "))
sub4 = int(input("Enter marks of Subject 4: "))
sub5 = int(input("Enter marks of Subject 5: "))


total = sub1 + sub2 + sub3 + sub4 + sub5
percentage = (total / 500) * 100

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "Fail"

print("\nStudent Result")
print("Total Marks:", total, "/ 500")
print("Percentage:", round(percentage, 2), "%")
print("Grade:", grade)
print("Thank you for using the Grade Evaluator!")
