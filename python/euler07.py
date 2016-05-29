"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
import euler03
import time

start = time.time()
sieve = euler03.sieve # Using sieve function from problem 3

def solve_it():
	p_list = sieve(200000) # This is assuming the 10 001st prime is < 200000
	return p_list[10000] # Returning the 10 001st prime number

print solve_it()
print time.time() - start