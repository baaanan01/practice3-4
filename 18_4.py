def bracket_check(test_string):
	count = 0
	for i in test_string:
		if i == '(':
			count +=1
		elif i == ')':
			count -= 1
		if count < 0:
			break
	print('YES') if count == 0 else print('NO')