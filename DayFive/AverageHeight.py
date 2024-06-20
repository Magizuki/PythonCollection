student_heights = input().split()
print(student_heights)
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)
total = 0
count = 0
for n in range(0, len(student_heights)):
    total += student_heights[n]
    count += 1
avg = float(total / count)
print('%.2f' %avg)
