import math
def roots_of_quadratic_equation(a,b,c):
	discr = b ** 2 - 4 * a * c	
	if discr > 0:
		x1 = (-b + math.sqrt(discr)) / (2 * a)
		x2 = (-b - math.sqrt(discr)) / (2 * a)
		print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
	elif discr == 0:
		x = -b / (2 * a)
		print("x = %.2f" % x)
	else:
		print("no roots")