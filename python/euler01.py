"""
Problem 1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

def multiples(max_multiple): # natural numbers < max_mutiple and multiples of 3 or 5
    multiples = []
    for i in range(3, max_multiple):
        if i%3==0 or i%5==0:
            multiples.append(i)
    return sum(multiples)

print multiples(10)
print multiples(1000)


