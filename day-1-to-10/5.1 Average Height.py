# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
sum = 0
no = 0
for height in student_heights:
	no += 1
	sum += height
	
avg_height = sum / no
avg_height = round(avg_height)

print(f'Average height of students is {avg_height}')

