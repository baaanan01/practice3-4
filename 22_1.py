lower = ['а','б','в','г','д','е','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я']
upper = ['А','Б','В','Г','Д','Е','Ж','З','И','Й','К','Л','М','Н','О','П','Р','С','Т','У','Ф','Х','Ц','Ч','Ш','Щ','Ъ','Ы','Ь','Э','Ю','Я']
def  encrypt_caesar(msg, shift):
	strin = ""
	for i in msg:
		if i in lower:
			ii = lower.index(i) % len(lower)
			strin += lower[(ii + shift) % len(lower)]
		elif i in upper:
			ii = upper.index(i) % len(upper)
			strin += upper[(ii + shift) % len(upper)]
		else:
			strin += i
	return strin

def decrypt_caesar(msg, shift):
	strin = ""
	for i in msg:
		if i in lower:
			ii = lower.index(i)
			strin += lower[ii - shift]
		elif i in upper:
			ii = upper.index(i)
			strin += upper[ii - shift]
		else:
			strin += i
	return strin