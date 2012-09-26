# Triangle numbers: T(n) = n * (n + 1) / 2
# Pentagonal numbers: P(n) = n * (3n - 1) / 2
# Hexagonal numbers: H(n) = n * (2n - 1)
#
# T(285) = P(165) = H(143) = 40755
#
# Task: Find the next triangle number that is also pentagonal and hexagonal.

# List all triangle numbers that are also pentagonal and hexagonal and that
# are below limit!

# List all triangle numbers H(n) that are also pentagonal and hexagonal, for
# 1 <= n < limit
def enumerateSpecialNum(limit):
    triangle = set([(n * (n + 1)) // 2 for n in range(1, limit)])
    pentagonal = set([(n * (3 * n - 1)) // 2 for n in range(1, limit)])
    hexagonal = set([n * (2 * n - 1) for n in range(1, limit)])

    intersect = triangle & pentagonal & hexagonal

    for x in intersect:
        print(x)
    
