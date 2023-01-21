# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
highScore = 0
for i in range(0, len(student_scores)-1):
    if student_scores[i] > student_scores[i+1] and student_scores[i] > highScore:
        highScore = student_scores[i]
    elif student_scores[i+1] > student_scores[i] and student_scores[i+1] > highScore:
        highScore = student_scores[i+1]

print(f"The highest score in the class is: {highScore}")