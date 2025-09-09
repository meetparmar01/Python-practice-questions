marks = int(input("Enter marks (0-100): "))

match marks:
    case m if m >= 90:
        grade = "A"
    case m if m >= 75:
        grade = "B"
    case m if m >= 60:
        grade = "C"
    case m if m >= 40:
        grade = "D"
    case _:
        grade = "F"

print("Grade:", grade)