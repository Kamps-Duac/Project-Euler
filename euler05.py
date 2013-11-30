"""
2520 is the smallest number that can be divided by each of the numbers 
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all 
of the numbers from 1 to 20?
"""

import time
start = time.time()

def solve_it():
	return generate()

def generate():
	ground = True
	base = 20
	d = range(2, 21)
	while ground:
		base += 20
		ground = False
		for divs in d:
			if base % divs != 0:
				ground = True
	return base

print solve_it()
print time.time() - start