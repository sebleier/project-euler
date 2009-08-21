"""
    Problem #3:
        The prime factors of 13195 are 5, 7, 13 and 29.

        What is the largest prime factor of the number 600851475143?

    Solution:
        You only need to test values from 2 to floor(sqrt(n)) since any number
        after sqrt(n) has already had its cofactors tested.

        Refer to http://mathworld.wolfram.com/DirectSearchFactorization.html
        for proof.
"""
from math import floor, sqrt
from functions import is_prime

n = 600851475143

begin = int(floor(sqrt(n)))

# omit the firt number if it is even, so you can decrement by 2
if begin % 2 == 0:
    begin -= 1

for i in xrange(begin, 2, -2):
    # check if divisible first because it is faster, then primality
    if n % i == 0 and is_prime(i):
        print "answer: %d" % i
        break

