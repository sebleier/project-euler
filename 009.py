"""
    Problem #9:
        A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
        a^(2) + b^(2) = c^(2)

        For example, 3^(2) + 4^(2) = 9 + 16 = 25 = 5^(2).

        There exists exactly one Pythagorean triplet for which a + b + c = 1000.
        Find the product abc.

        a = 2*m*n
        b = m**2 - n**2
        c = m**2 + n**2
"""


# A little faster to compute, without using sqrt.  But still brute forcing it.
# This really is an O(1) calculation while a little algebra.
for m in xrange(1,1000):
    for n in xrange(1,1000):
        if 2*m * (n + m) == 1000:
            a = 2*m*n
            b = m**2 - n**2
            c = m**2 + n**2
            if not (a < b < c):
                continue
            print "answer: %s" % (a * b * c)
        if 2*m * (n + m) > 1000:
            continue
