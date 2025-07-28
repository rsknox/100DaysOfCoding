student_scores = [150, 142.185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86]
max = 0
length = len(student_scores)
print(length)
for i in range(0, length-1):
    score = int(student_scores[i])
    if score > max:
        max = score
print(max)


