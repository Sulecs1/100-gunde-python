student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99, 
    "Draco": 74,
    "Neville": 62,
}

#TODO-1: Create an empty dictionary called student_grades.

student_grades = {}


#TODO-2: Write your code below to add the grades to student_grades.👇

for name in student_scores:
    if 90 < student_scores[name] <= 100:
        student_grades[name] = "Outstanding"
    elif 80 < student_scores[name] <= 90:
        student_grades[name] = "Exceeds Expectations"
    elif 70 < student_scores[name] <= 80:
        student_grades[name] = "Acceptable"
    elif 0 <= student_scores[name] <= 70:
        student_grades[name] = "Fail"
    else:
        student_scores[name] = "Unvaild Score"

print(student_grades)





