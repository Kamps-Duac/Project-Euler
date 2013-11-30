"""
A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 
9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def solve_it():
	palindrome, product = find_pal()
	print "The largest palindrome made from the product of two 3-digit numbers is:"
	print "%d = %s" % (palindrome, product)

def find_pal():
	palindrome = 0
	for i in range(999, 100, -1):
		for j in range(999, 100, -1):
			p = i*j
			if is_pal(p) and p > palindrome:
				palindrome = p
				p_n = '%d * %d' %(i, j)
	return palindrome, p_n

def is_pal(p):
	s_p = str(p)
	for d in s_p:
		if len(s_p) == 6:
			return s_p[0]==s_p[-1] and s_p[1]==s_p[-2] and s_p[2] == s_p[-3]
		else:
			return s_p[0]==s_p[-1] and s_p[1]==s_p[-2]

solve_it()