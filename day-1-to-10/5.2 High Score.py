# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

largest_number = student_scores[0]

for i in student_scores:
	if i > largest_number:
		largest_number = i

print(f'Largest number is {largest_number}')