def transpose(matrix):
	matrix[:] = [list(x) for x in zip(*matrix)]