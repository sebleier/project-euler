from math import sqrt, log, floor


def F(n):
    """The nth number in the fibonacci sequence based off of Binet's Formula"""
    return int(((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5)))

def m_ord(n, r):
    """

    """
    for k in xrange(1, n):
        if n**k % r == 1:
            return k

def gcd(a, b):
    """
        the function to calculate the GCD
    """
    a, b = max(a, b), min(a,b)
    if a == b:
        return a
    for i in xrange(b, 1, -1):
        if 0 in (a % i, b % i):
            return i

# the function to calculate the LCM
def lcm(a, b):
    return a * b / gcd(a, b)

def is_prime(n):
    for i in xrange(3, int(floor(sqrt(n))), 2):
        if n % i == 0:
            return False
    return True

def totient(n):
     """
        Compute the number of positives < n that are
        relatively prime to n -- good solution!
     """
     tot, pos = 0, n-1
     while pos>0:
        if gcd(pos,n)==1: tot += 1
        pos -= 1
     return tot

def aks(n):
    """ Test primality using the AKS primality test """

    for a in xrange(1, n):
        for b in xrange(2, n):
            num = a**b
            if num == n:
                return False
            if num > n:
                break

    for r in xrange(2, n):
        if m_ord(n, r) > log(n, 2):
            break

    for a in xrange(1, r):
        if 1 < gcd(a,n) < n:
            return False

    if n <= r:
        return True


    return True

def primes(n):
    """Generate a list of the prime numbers [2, 3, ... m] where
    m is the largest prime <= n."""
    n = n + 1
    sieve = range(n)
    sieve[:2] = [0, 0]
    for i in xrange(2, int(n**0.5)+1):
        if sieve[i]:
            for j in xrange(i**2, n, i):
                sieve[j] = 0
    # Filter out the composites, which have been replaced by 0's
    return [p for p in sieve if p]


