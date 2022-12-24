from get_input import get_input
import numpy as np

file_path = get_input(8)

with open(file_path) as f:
	data = np.array([list(x.strip()) for x in f])

data = data.astype(int)

def left_to_right_vis(data):
	is_visible = np.zeros(data.shape)
	for i in range(data.shape[0]):
		curr_max = data[i, 0]
		is_visible[i, 0] = 1
		for j in range(1, data.shape[1]):
			if data[i,j] > curr_max:
				curr_max = data[i,j]
				is_visible[i,j] = 1
	return is_visible


def rot(k):
	return lambda x: np.rot90(x, k)

left_right_tfs = [(rot(k), rot(4-k)) for k in range(4)]
is_visible = np.zeros(data.shape)

for fn, invfn in left_right_tfs:
	is_visible += invfn(left_to_right_vis(fn(data)))

print((is_visible > 0).sum())


def up_scenic_score(data):
	scenic_score = np.zeros(data.shape)
	for i in range(data.shape[0]-1):
		for j in range(data.shape[1]):
			max_yet = data[i+1, j]
			scenic_score[i+1, j] += 1
			# if max_yet > data[i,j]: continue
			for k in range(i+2, data.shape[0]):
				if data[k, j] > max_yet:
					scenic_score[k, j] += 1
					max_yet = data[k, j]
				# if max_yet > data[i,j]: break
	return scenic_score

scenic_score = np.ones(data.shape)
for fn, invfn in left_right_tfs:
	scenic_score *= invfn(up_scenic_score(fn(data)))

print(scenic_score.max())