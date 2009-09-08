"""
    Problem #15:
        Starting in the top left corner of a 2+2 grid, there are 6 routes
        (without backtracking) to the bottom right corner.

        How many routes are there through a 20x20 grid?
"""

from functions import nCk

n = 40
k = 20
print nCk(n, k)

