from get_input import get_input

file_path = get_input(1)

def read_elf(x):
	return map(int, x.split("\n"))

with open(file_path) as f:
	x = map(read_elf, f.read().strip().split("\n\n"))

def answer1(x):
	return max(map(sum, x))

def answer2(x):
	return sorted(map(sum, x))[-3:]

print(sum(answer2(x)))

	