def line(s, t):
	x = float(t.split(";")[0])	
	y = float(t.split(";")[1])
	k, t = s.split('x')
	k, t = int(k), int(t)
	y2 = k * x + t
	y2 != y
	print(y2 == y)

line("5x-10", "5;-9")