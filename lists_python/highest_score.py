student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62
}

student_grades = {}

for names, scores in student_scores.items():
    if 91 <= scores <= 100:
        student_grades[names] = "Outstading"
    elif 81 <= scores <= 90:
        student_grades[names] = "Exceeds Expectations"
    elif 71 <= scores <= 80:
        student_grades[names] = "Acceptable"
    else:
        student_grades[names] = "Fail"
print(student_grades)
