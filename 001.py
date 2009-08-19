"""
    Problem #1:
        If we list all the natural numbers below 10 that are multiples of 3 or
        5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

        Find the sum of all the multiples of 3 or 5 below 1000.

    Solution:
        Since 1 + 2 + 3 ... + n = n * (n + 1) / 2
        and 3 + 6 + 9 ... = 3(1) + 3*(3) + 3*(6) = 3 * (1 + 2 + 3...)

    Thanks to Akrito for some help
"""
ceiling = 999
nums = (3, 5, -15)

def scaled_divergent_series(x):
    n = ceiling / x
    divergent_series = (n * (n + 1) / 2)
    return x * divergent_series

print sum(map(scaled_divergent_series, nums))
