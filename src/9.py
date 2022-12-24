from get_input import get_input
import numpy as np

file_path = get_input(9)

with open(file_path) as f:
	data = [x.strip().split(" ") for x in f]

rope = [(0,0) for i in range(10)]

def predict_next(head, tail, direc):
	x,y = head
	a,b = tail
	d1, d2 = abs(x-a), abs(y-b)
	if max(d1, d2) <= 1: return tail
	if d1 != 0:	a += (x-a)//d1
	if d2 != 0:	b += (y-b)//d2
	return (a,b)

visited = {rope[-1]}

direction_dict = {
	"U": (0, 1),
	"D": (0, -1),
	"L": (-1, 0),
	"R": (1, 0)
}

for d, m in data:
	m = int(m)
	x,y = direction_dict[d]
	print(rope)
	for _ in range(m):
		rope[0] = (rope[0][0] + x, rope[0][1] + y)
		for i in range(len(rope) - 1):
			rope[i+1] = predict_next(rope[i], rope[i+1], (x,y))

		visited.add(rope[-1])

print(rope)
print(len(visited))


