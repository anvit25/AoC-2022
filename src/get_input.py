import os
from os.path import exists
import requests


YEAR = 2021
SESSION = os.environ["AOC_SESSION"]
COOKIE = dict(session = SESSION)

def get_input(x: int):
	file_path = f"..\\input\\{x}.txt"

	if not exists(file_path): 
		url = f"https://adventofcode.com/{YEAR}/day/{x}/input"
		r = requests.get(url, cookies=COOKIE)
		with open(file_path, "wb") as f:
			f.write(r.content)
	
	return file_path
