from get_input import get_input

file_path = get_input(6)

with open(file_path) as f:
	x = f.read()

for i in range(14, len(x)):
	if len(set(x[i-14:i])) == 14:
		print(i)
		break

