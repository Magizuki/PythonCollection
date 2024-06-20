student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermoinie": 99,
    "Draco": 74,
    "Neville": 62
}

grade_list = {}
for key in student_scores:
    if student_scores[key] >= 91:
        grade_list[key] = "Outstanding"
    elif student_scores[key] >= 81:
        grade_list[key] = "Exceeds Expectations"
    elif student_scores[key] >= 71:
        grade_list[key] = "Acceptable"
    elif student_scores[key] <= 70:
        grade_list[key] = "Fail"
    
print(grade_list)