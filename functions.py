from math import sqrt, log, log10, floor, ceil, factorial as f

def F(n):
    """The nth number in the fibonacci sequence based off of Binet's Formula"""
    return int(((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5)))

def is_prime(n):
    if n in (1,2):
        return True
    if n % 2 == 0:
        return False
    for i in xrange(3, int(ceil(sqrt(n))) + 1, 2):
        if n % i == 0:
            return False
    return True

def old_sieve(limit):
    """
        A relatively space and time efficient method to return all primes up
        to a specified limit.

        Since all primes after 3 are of the form 6 * k +- 1, you only need to
        check those values for their primality.
    """
    p = [2,3]
    for i in xrange(1,limit):
        if is_prime(6 * i - 1):
            p.append(6 * i - 1)
        if is_prime(6 * i + 1):
            p.append(6 * i + 1)
    return p

def raw_sieve(m):
    nums = range(m)
    nums[1] = 0
    i = 0
    while i**2 < m:
        if nums[i] == 0:
            i += 1
            continue
        # The next non-zero should be prime
        p = nums[i]

        # Zero out all the multiples of p, starting at the square (optimization)
        j = p
        r = j * p
        while r < m:
            nums[r] = 0
            j += 1
            r = j * p
        i += 1
    return nums

def sieve(m):
    return [x for x in raw_sieve(m) if x != 0]

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

def prime_factors(n):
    factors = []
    while not is_prime(n):
        s = sieve(int(ceil(sqrt(n))))
        for prime in s:
            if n % prime == 0:
                factors.append(prime)
                n /= prime
                break
    factors.append(n)
    return factors

# the function to calculate the LCM
def lcm(*nums):
    c = {}
    for n in nums:
        pf = prime_factors(n)
        for p in pf:
            if p not in c.keys():
                c[p] = 0
            c[p] = max(c[p], pf.count(p))
    prod = 1
    for n in c.keys():
        prod *= n**c[n]
    return prod

def m_ord(n, r):
    """

    """
    for k in xrange(1, n):
        if n**k % r == 1:
            return k

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
    """
        Test primality using the AKS primality test
        TODO: make work :)
    """

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

def digit(n, i):
    return (n / (10 ** i)) % 10

def num_digits(n):
    return int(floor(log10(n)))+1

# distinguishes between string and numbers
def is_palindromic(n):
    if isinstance(n, str):
        return str(n) == str(n)[::-1]
    d = num_digits(n)
    for i, j in zip(xrange(d), xrange(d-1, -1, -1)):
        if digit(n, i) != digit(n, j):
            return False
        if i >= j:
            return True
    return True

def nCk(n, k):
    return f(n) / (f(k)*f(n - k))
