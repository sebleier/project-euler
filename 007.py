"""
    Problem #7:
        By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can
        see that the 6^(th) prime is 13.

        What is the 10001^(st) prime number?

"""
from functions import pi, is_prime


n = 0
for i in xrange(2, 1000000):
    if is_prime(i):
        n += 1
    if n == 10001:
        print i
        break

