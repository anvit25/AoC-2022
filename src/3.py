from get_input import get_input

file_path = get_input(3)

with open(file_path) as f:
	data = [x.strip() for x in f]


def char_to_priority(c):
	if ord(c) <= 90:
		return ord(c) - 64 + 26
	return ord(c) - ord('a') + 1

score1 = 0
for ruck in data:
	n = len(ruck)
	c1 = ruck[:n//2]
	c2 = ruck[n//2:]
	char = list(set(c1).intersection(c2))[0]
	score1 += char_to_priority(char)

print(score1)

score2 = 0
for i in range(0, len(data), 3):
	e1, e2, e3 = data[i:i+3]
	c = list(set(e1).intersection(e2).intersection(e3))[0]
	score2 += char_to_priority(c)

print(score2)

