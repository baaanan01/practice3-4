def fibonachhi(i):
	fib1 = fib2 = 1
	n = 2
	if i == 1 or i == 2:
		sum = 1
	while n < i:
		sum = fib2 + fib1
		fib1 = fib2
		fib2 = sum
		n += 1
	return sum
def golden_ratio(i):
	print (fibonachhi(i + 1) / fibonachhi(i))

golden_ratio(2)