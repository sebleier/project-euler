"""
    Problem #2:
        Each new term in the Fibonacci sequence is generated by adding the
        previous two terms. By starting with 1 and 2, the first 10 terms
        will be:

        1, 2, 3, 5, 8, 13, 21, 34, 55, 89...

        Find the sum of all the even-valued terms in the sequence which do not
        exceed four million.

        x:    0, 1, 2, 3, 4, 5, 6,  7,  8,  9, 10, 11
        F(x): 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89
              ^        ^        ^           ^

        Since every x divisble by 3 in the fibonacci sequence is even and
        all others even, you only need to add those numbers.

"""

from functions import F
import sys

limit = int(sys.argv[1])

sum = 0
for i in xrange(0, limit, 3):
    if F(i) >= limit:
        print "answer: " + str(sum)
        break
    sum += F(i)



