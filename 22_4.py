import math

def  solve(*coefficients):
    a = b = c = 0
    if len(coefficients) == 0 or len(coefficients) > 3:
        return None
    elif len(coefficients) == 2:
        b = coefficients[0]
        c = coefficients[1]
    elif len(coefficients) == 3:
        a = coefficients[0]
        b = coefficients[1]
        c = coefficients[2]
    x1 = (-b+math.sqrt(b**2-4*a*c))/(2*a)
    x2 = (-b-math.sqrt(b**2-4*a*c))/(2*a)
    return x1, x2
	
print(sorted(solve(1, 2, 1)))