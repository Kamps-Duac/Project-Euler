"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""

import time
start = time.time()

def solve_it(max_int): # where number is the number to be factored
	primes = sieve(max_int)
	print "\nTo generate primes, it took", time.time() - start, "seconds.\n"
	return prime_factor(max_int, primes)[-1]

def prime_factor(max_int, primes):
	prime_factors = []
	sqr_max = int(round(max_int**0.5))
	for n in xrange(3, sqr_max+1, 2):
		if max_int%n == 0:
			if n in primes:
				prime_factors.append(n)
	return prime_factors

def sieve(n):
	"Generate a list of primes <= n, using the Sieve of Eratosthenes"
	n1 = n + 1
	s = range(n1)
	s[1] = 0
	sqrt_n = int(round(n**0.5))
	for i in xrange(2, sqrt_n + 1):
		if s[i]:
			s[i*i: n1: i] = [0] * len(xrange(i*i, n1, i))
	return filter(None, s)

# num = 13195 # number to be factored
# answer = solve_it(num)
# print "The largest prime factor of %r is" % num, str(answer) + '.', '\n' # Note: this is very slowwwwwww

# print "The result took", time.time() - start, "seconds to find.\n"