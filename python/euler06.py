"""
The sum of the squares of the first ten natural numbers is,

1**2 + 2**2 + ... + 10**2 = 385

The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)**2 = 55**2 = 3025
Hence the difference between the sum of the squares of the 
first ten natural numbers and the square of the sum is 3025 - 385 = 2640.
Find the difference between the sum of the squares of the first 
one hundred natural numbers and the square of the sum.
"""

def solve_it(how_many):
	return square_of_sum(how_many) - sum_of_squares(how_many)

def sum_of_squares(how_many):
	squares = []
	for n in range(1, how_many + 1):
		squares.append(n**2)
	return sum(squares)

def square_of_sum(how_many):
	nn = range(1, how_many + 1)
	return sum(nn)**2

print solve_it(100)