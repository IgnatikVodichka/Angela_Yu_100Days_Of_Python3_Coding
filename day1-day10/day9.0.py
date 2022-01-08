

student_scores = {"Harry": 81,
                  "Ron": 78,
                  "Hermione": 99,
                  "Draco": 74,
                  "Snape": 62,
                  }


student_grades = {}


for student in student_scores:
    score = student_scores[student]
    if score > 91:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds Expectations"
    elif score > 71:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

print(student_grades)


'''
Another method
'''


# for key in student_scores:
#     student_grades[key] = student_scores[key]
#     if student_scores[key] in range(91, 101):
#         student_grades[key] = "Outstanding"
#     elif student_scores[key] in range(81, 91):
#         student_grades[key] = "Exceeds Expectations"
#     elif student_scores[key] in range(71, 81):
#         student_grades[key] = "Acceptable"
#     else:
#         student_grades[key] = "Fail"
# print(student_grades)
