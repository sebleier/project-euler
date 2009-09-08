"""
    Problem #18:
        By starting at the top of the triangle below and moving to adjacent numbers
        on the row below, the maximum total from top to bottom is 23.

                3
                7 4
                2 4 6
                8 5 9 3

        That is, 3 + 7 + 4 + 9 = 23.

        Find the maximum total from top to bottom of the triangle below:

                75
                95 64
                17 47 82
                18 35 87 10
                20 04 82 47 65
                19 01 23 75 03 34
                88 02 77 73 07 63 67
                99 65 04 28 06 16 70 92
                41 41 26 56 83 40 80 70 33
                41 48 72 33 47 32 37 16 94 29
                53 71 44 65 25 43 91 52 97 51 14
                70 11 33 28 77 73 17 78 39 68 17 57
                91 71 52 38 17 14 91 43 58 50 27 29 48
                63 66 04 68 89 53 67 30 73 16 69 87 40 31
                04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

        NOTE: As there are only 16384 routes, it is possible to solve this
        problem by trying every route. However, Problem 67, is the same challenge
        with a triangle containing one-hundred rows; it cannot be solved by brute
        force, and requires a clever method! ;o)

"""
t = []
tri = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""
for row in tri.split("\n"):
    t.append(map(int,row.split()))

def solve(t):
    t.reverse()
    for p, r in enumerate(t[0]):
        t[0][p] = [t[0][p]]
    for p, r in enumerate(t[:-1]):
        for (pi, i) in enumerate(r[0:-1]):
            j = t[p][pi + 1]
            pj = pi + 1
            a = []
            if sum(i) > sum(j):
                a.extend(i)
            else:
                a.extend(j)
            a.insert(0, t[p + 1][pi])
            t[p + 1][pi] = a
    t.reverse()
    return sum(t[0][0])

import datetime
t1 = datetime.datetime.now()
answer = solve(t)
t2 = datetime.datetime.now()
print answer
print "Time: %s" % str(t2 - t1)
