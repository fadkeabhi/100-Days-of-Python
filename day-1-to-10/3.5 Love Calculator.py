# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name = name1 + name2
name = name.lower()

#true
ctrue = 0
for i in 'true':
	ctrue += name.count(i)

clove = 0
for i in 'love':
	clove += name.count(i)

score = 10*ctrue + clove

if score < 10 or score > 90:
	print(f"Your score is {score}, you go together like coke and mentos.")
elif score > 40 and score < 50:
	print(f"Your score is {score}, you are alright together.")
else:
	print(f"Your score is {score}.")