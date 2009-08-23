"""
    Problem #5:
        2520 is the smallest number that can be divided by each of the numbers
        from 1 to 10 without any remainder.

        What is the smallest number that is evenly divisible by all of the
        numbers from 1 to 20?

    Solution:
        This is a least common multiple problem.

"""
from functions import lcm


max_range = 20
print lcm(*range(1, max_range + 1))
