height = float(input('Enter your height in m: '))
weight = float(input('Enter your weight in kg: '))

#calculate bmi

bmi = round(weight / height ** 2)

if bmi < 18.5:
	print(f'Your BMI is {bmi}, you are underweight')
elif bmi < 25:
	print(f'Your BMI is {bmi}, you have a normal weight')
elif bmi < 30:
	print(f'Your BMI is {bmi}, you are Overweight')
else:
	print(f'Your BMI is {bmi}, you are Obese')