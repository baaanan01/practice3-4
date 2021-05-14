def solve(*coefficients):
    roots = []
    lenght = len(coefficients)
    if lenght == 1:
        if coefficients[0] == 0:
            roots.append('all')
    if len(coefficients) == 2:
        b, c = coefficients[0], coefficients[1]
        roots.append(-c / b)
        print(*roots)
    if lenght == 3:
        a = coefficients[0]
        b = coefficients[1]
        c = coefficients[2]
        disc = b ** 2 - 4 * a * c
        if disc == 0:
            roots.append(-b / 2 * a)
        elif disc > 0:
            x1 = (-b + disc**0.5) / (a + a)
            x2 = (-b - disc**0.5) / (a + a)
            roots.append(x1)
            roots.append(x2)
    print(*roots)