"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a**2 + b**2 = c**2
For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.


Answer:
31875000
"""

import time
start = time.time()

def solve_it():
    for a in range(1, 998):
        for b in range(2,999):
            for c in range(3,1000):
                if is_triplet(a, b, c) and is_sum(a, b, c):
                    print a, b, c
                    return a*b*c
    

def is_triplet(a, b, c):
    return a**2 + b**2 == c**2 and c > b and b > a
    
def is_sum(a, b, c):
    return a + b + c == 1000

print solve_it()
print time.time() - start