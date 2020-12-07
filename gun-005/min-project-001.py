# Average Height

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

iter = 0
total_height = 0

for height in student_heights:
    total_height += height
    iter += 1

print(round(total_height / iter))