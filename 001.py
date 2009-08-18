"""
    Problem #1:
        If we list all the natural numbers below 10 that are multiples of 3 or 
        5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
        
        Find the sum of all the multiples of 3 or 5 below 1000.                 
"""
ceiling = 999
nums = (3, 5)

def scaled_divergent_series(x):
    n = ceiling / x 
    divergent_series = (n * (n + 1) / 2) 
    return x * divergent_series  

print sum(map(scaled_divergent_series, nums)) - scaled_divergent_series(15)
