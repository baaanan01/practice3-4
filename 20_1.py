ttext = ''
def translate(text):
	global ttext
	alpha = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я',
		'А', 'Е', 'Ё', 'И', 'О', 'У', 'Ы', 'Э', 'Ю', 'Я', ',', '.', '-']
	for i in range(len(text) - 1):
		if alpha.count(text[i]) == 0:
			ttext = ttext + text[i]
	ttext = ' '.join(ttext.split())
	return ttext