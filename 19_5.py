def prime(number):
	f = False
	if number > 1:
		for i in range(2, number):
			if(number % i) == 0:
				f = True
			break
	if f:
		print("Составное число")
	else:
		print("Простое число")