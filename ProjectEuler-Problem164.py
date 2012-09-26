# Find the number of n-digit natural numbers A such that no three consecutive
# digits of A have a sum greater than 9.

# Let f(n, B) = the number of n-digit natural numbers A (leading zeros allowed)
# with B is the number formed by the first two digits of A such that
# no three consecutive digits of A have a sum greater than a specified
# constant C (Here C = 9).

# Recurrence relation:
#   f(n, B) = sum{f(n - 1, D)} where D = 10 * (B % 10) + H for all H such that
#                  0 <= H <= 9 and B % 10 + H + floor(B / 10) <= C.

# Base cases: f(n, B) = 1 if n < 3 and B % 10 + floor(B / 10) <= C
#             f(n, B) = 0 if n < 3 and B % 10 + floor(B / 10 > C

# Let g(n, B) = the number of n-digit natural numbers A (no leading zeros)
# with B is the number formed by the first two digits of A such that
# no three consecutive digits of A have a sum greater than a specified
# constant C (Here C = 9).
#
# g(n, B) = sum(f(n, P)) where 10 <= P <= 99

# Methodology: Using memoization to prevent recomputation.
MEMO_TABLE = []

def countSpecialNum(numDigit, upperLimit):
    initializeMemoTable(numDigit)

    count = 0
    for firstTwoDigit in range(10, 100):
        count += f(numDigit, firstTwoDigit, upperLimit)

    return count

def initializeMemoTable(n):
    global MEMO_TABLE
    
    MEMO_TABLE = [[-1] * 100 for row in range(0, n + 1)]
    
def f(numDigit, firstTwoDigit, upperLimit):
    if numDigit < 3:
        if firstTwoDigit // 10 + firstTwoDigit % 10 <= upperLimit:
            return 1
        else:
            return 0
    if MEMO_TABLE[numDigit][firstTwoDigit] >= 0:
        return MEMO_TABLE[numDigit][firstTwoDigit]
    
    mySum = 0
    firstDigit = firstTwoDigit // 10
    secondDigit = firstTwoDigit % 10

    thirdDigit = 0
    while thirdDigit < 10 and thirdDigit + firstDigit + secondDigit <= upperLimit:
        mySum += f(numDigit - 1, secondDigit * 10 + thirdDigit, upperLimit)
        thirdDigit += 1

    MEMO_TABLE[numDigit][firstTwoDigit] = mySum

    return mySum
