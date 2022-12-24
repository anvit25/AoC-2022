from get_input import get_input
import numpy as np

file_path = get_input(10)

with open(file_path) as f:
	data = [x.strip() for x in f]

register = [1]

for i, command in enumerate(data):
	if command == "noop": 
		register.append(0)
	elif command[:4] == "addx":
		n = int(command.split(" ")[1])
		register.append(0)
		register.append(n)
	else: raise ValueError(f"Unknown command {command}")

register = np.cumsum(register)

useful = register[np.arange(19, 240, 40)]
print(sum(useful*(1+np.arange(19, 240, 40))))


rows = []
for i in range(0, 201, 40):
	curr = ""
	for j in range(40):
		if abs(register[i+j]-j) <= 1:
			curr = curr + "#"
		else: curr = curr + "."
	rows.append(curr)

for row in rows:
	print(row)
