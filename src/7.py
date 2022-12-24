from get_input import get_input

file_path = get_input(7)

with open(file_path) as f:
	x = [y.strip() for y in f][1:]

class Tree:
	def __init__(self, val, parent = None, size = None):
		self.nodes = []
		self.parent = parent
		self.val = val
		self.size = size

	def add_folder(self, name, move = False):
		obj = Tree(name, parent = self)
		self.nodes.append(obj)
		if move: return obj
		return self

	def move_to_folder(self, name):
		if name == "..": return self.parent
		for node in self.nodes:
			if node.val == name:
				return node
		return self.add_folder(name, True)

	def add_file(self, file_str):
		a, b = file_str.split(" ")
		obj = Tree(b, parent = self, size = int(a))
		self.nodes.append(obj)
		return self

	def compute_size(self):
		if self.size is not None:
			return self.size
		self.size = 0
		for node in self.nodes:
			self.size += node.compute_size()
		return self.size

	def apply_command(self, x):
		if x[0] == '$':
			if "$ cd" in x:
				return self.move_to_folder(x[5:])
			elif x == "$ ls":
				return self
			else:
				raise ValueError(f"Unknown command {x}")

		elif x[:3] == "dir":
			return self.add_folder(x[4:])

		elif x[0] in "0123456789":
			return self.add_file(x)

		else: raise ValueError(f"Unknown command {x}")

	def __repr__(self):
		return str((self.val, self.size, self.nodes))

directory = Tree('/')
curr = directory

for command in x:
	curr = curr.apply_command(command) 


directory.compute_size()

def answer1(tree):
	total_size = 0
	if tree.size <= 100000:
		total_size = tree.size

	if not tree.nodes: return 0
	for node in tree.nodes:
		total_size += answer1(node)
	return total_size

print(answer1(directory))

total = 70_000_000
req = 30_000_000
used = directory.size
available = total - used
to_free = req - available

def valid_directories2(tree):
	if tree.size < to_free: return []
	valid = [(tree.val, tree.size)]
	for node in tree.nodes:
		valid += valid_directories2(node)
	return valid

print(sorted(valid_directories2(directory), key = lambda x: x[1]))