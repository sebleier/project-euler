"""
    Problem #4:
        A palidromic number reads the same both ways.  The largest palidrome
        made from the profuct of two 2-digit numbers is 9009 = 91 x 99.

        Find the largest palindrome made from the product of two 3-digit numbers.

        Note: Probably can be done in a O(1) manner using some algebra

"""
from functions import is_palindromic

i, j = 100, 1000 # range of three digit numbers
r, s = 100, 1000
p = []
for n in range(j, i-1, -1):
    for k in range(s, r-1, -1):
        product = n * k
        if is_palindromic(product):
            p.append(product)

print max(p)

