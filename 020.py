"""
    Problem #20:
        n! means n x (n - 1) x ... x 3 x 2 x 1

        Find the sum of the digits in the number 100!
"""

from math import factorial as f

print sum(map(int, list(str(f(100)))))
