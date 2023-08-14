import random
n = random.randint(1,100)
while True:
	g = int(input("猜數字"))
	if g == n:
		print("猜中")
		break
	elif g < n:
		print("比答案小")
	else:
		print("比答案大")