from math import sqrt


def F(n):
    "The nth number in the fibonacci sequence based off of Binet's Formula"
    return int(((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5)))
