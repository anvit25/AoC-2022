from get_input import get_input

file_path = get_input(2)

wins = {
	'A': {'X': 0, 'Y': 1, 'Z':-1},
	'B': {'X':-1, 'Y': 0, 'Z': 1},
	'C': {'X': 1, 'Y':-1, 'Z': 0},
}
scores = {-1:0, 0:3, 1:6}
bonus = {'X':1, 'Y':2, 'Z':3}


with open(file_path) as file:
	data = [x.strip().split(" ") for x in file]

score1 = 0
for match in data:
	o, p = match
	score1 += scores[wins[o][p]] + bonus[p]
print(score1)


score2 = 0
for match in data:
	o, p = match
	curr = wins[o]
	if p == "X":
		p = [k for k,v in curr.items() if v == -1][0]
	elif p == "Y":
		p = [k for k,v in curr.items() if v == 0][0]
	elif p == "Z":
		p = [k for k,v in curr.items() if v == 1][0]
	score2 += scores[wins[o][p]] + bonus[p]
print(score2)