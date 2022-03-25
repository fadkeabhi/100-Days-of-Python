import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
def ptimg(i):
	if i == 'r':
		op = rock
	elif  i == 'p':
		op = paper
	else:
		op = scissors
	print(op)


while True:
	ui = input('Enter your choice r-rock p-paper s-scissors')
	if ui not in ['r','s','p']:
		print('please input valid values')
		continue
	print('your choice:')
	ptimg(ui)
	
	ci = random.choice(['r','p','s'])
	print('Computer choice')
	ptimg(ci)
	
	if ui == ci:
		print('There is draw')
	elif (ui == 'r' and ci =='s') or (ui == 's' and ci =='p') or (ui == 'p' and ci =='r'):
		print('You win')
	else:
		print('You lose')
	if input('Do you want to play again.(y/n) ') == 'n':
		break