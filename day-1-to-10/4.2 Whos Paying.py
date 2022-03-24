import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

no_of_items = len(names)

rand_choice = random.randint(0,no_of_items-1)
print(f'{names[rand_choice]} is going to pay today.')