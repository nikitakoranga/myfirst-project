# student_marks_calculator.py

def calculate_total(marks):
    return sum(marks)

def calculate_average(marks):
    return sum(marks) / len(marks)

def get_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"

print("📚 Student Marks Calculator")

# Take marks input for 5 subjects
marks = []
for i in range(1, 6):
    mark = float(input(f"Enter marks for Subject {i}: "))
    marks.append(mark)

# Calculations
total = calculate_total(marks)
average = calculate_average(marks)
grade = get_grade(average)

# Output results
print("\n🎓 Result Summary:")
print(f"Total Marks: {total}/500")
print(f"Average Marks: {average:.2f}")
print(f"Grade: {grade}")
