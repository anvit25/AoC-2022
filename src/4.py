from get_input import get_input

file_path = get_input(4)

def read_line(x):
	return [[int(z) for z in y.split('-')] for y in x.split(',')]

with open(file_path) as f:
	data = [read_line(x.strip()) for x in f]

def check1(x):
	r1, r2 = x
	r1l, r1r = r1
	r2l, r2r = r2

	if r2l <= r1l <= r1r <= r2r:
		return True
	if r1l <= r2l <= r2r <= r1r:
		return True
	return False

def check2(x):
	r1, r2 = x
	r1l, r1r = r1
	r2l, r2r = r2

	ans = min(r1r, r2r) - max(r1l, r2l) + 1

	return ans > 0

print(sum([check2(x) for x in data]))

