import numpy as np
import re

from get_input import get_input

file_path = get_input(5)

with open(file_path) as f:
	stack, rules = f.read().split("\n\n")


stack = [list(x[1::4]) for x in stack.split("\n")]
stack = np.array(stack).transpose()[:, :-1]
stack = [" "]+[list("".join(x).strip()) for x in stack]

def extract_nums(s):
	return list(map(int, re.findall(r'\d+', s)))

rules = list(map(extract_nums, rules.strip().split("\n")))

for rule in rules:
	a, b, c = rule
	to_move = stack[b][:a]
	stack[b] = stack[b][a:]
	stack[c] = to_move[::] + stack[c]

print("".join([x[0] for x in stack]))