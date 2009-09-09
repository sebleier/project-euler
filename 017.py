"""
    Problem #17:
        If the numbers 1 to 5 are written out in words: one, two, three, four,
        five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

        If all the numbers from 1 to 1000 (one thousand) inclusive were written
        out in words, how many letters would be used?

        NOTE: Do not count spaces or hyphens. For example, 342 (three hundred
        and forty-two) contains 23 letters and 115 (one hundred and fifteen)
        contains 20 letters. The use of "and" when writing out numbers is in
        compliance with British usage.
"""
ones = [
    "",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]
teens = [
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen",
]
tens = [
    "twenty",
    "thirty",
    "forty",
    "fifty",
    "sixty",
    "seventy",
    "eighty",
    "ninety"
]
hundreds = [
    "",
    "onehundred",
    "twohundred",
    "threehundred",
    "fourhundred",
    "fivehundred",
    "sixhundred",
    "sevenhundred",
    "eighthundred",
    "ninehundred",
]
thousand = "thousand"
s = 0
for h in hundreds:
    if h != "":
        a = "and"
    else:
        a = ""
    for o in ones:
        if h != "" and o != "":
            a = "and"
        else:
            a = ""
        print h + a + o
        s += len(h + a + o)
    for t in teens:
        print h + a + t
        s += len(h + a + t)
    if h != "":
        a = "and"
    else:
        a = ""
    for t in tens:
        for o in ones:
            print h + a + t + o
            s += len(h + a + t + o)
print ones[1] + thousand
s += len(ones[1] + thousand)
print s

