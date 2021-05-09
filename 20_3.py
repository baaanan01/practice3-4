oldjokes = list()
def print_only_new(message):
	global oldjokes
	if message not in oldjokes:
		oldjokes.append(message)
		print(message)