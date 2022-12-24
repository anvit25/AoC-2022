import os
from os.path import exists
import requests

YEAR = 2022

with open("SESSION") as file:
	COOKIE = dict(session = file.readline())

def get_input(x: int):
	# wrt the main directory
	file_path = f"..\\input\\{x}.txt"

	if not exists(file_path): 
		url = f"https://adventofcode.com/{YEAR}/day/{x}/input"
		r = requests.get(url, cookies=COOKIE)
		with open(file_path, "wb") as f:
			f.write(r.content)
	
	return file_path
