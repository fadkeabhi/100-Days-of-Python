cal_from = 0
cal_up_to = 100
sum = 0
for i in range(cal_from,cal_up_to + 1):
	if i % 2 == 0:
		sum += i

print(f'sum of even numbers from {cal_from} to {cal_up_to} is {sum}')