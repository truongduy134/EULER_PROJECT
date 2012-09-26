# For each natural number n, reverse(n) is a natural number obtained by
# reversing the digits in n.
#
# A natural number n is reversible if
#   1) n is not a multiple of 10
#   2) n + reverse(n) consists entirely of odd decimal digits!
#
# Count the number of reversible numbers below 10^9

def countNumReversible(limit):
     count = 0
     for n in range(1, limit):
         if isReversible(n):
             count += 1

     return count

def isReversible(N):
    if N % 10 == 0:
        return False
    return containAllOddDigit(N + reverseNum(N))

def containAllOddDigit(N):
    if N == 0:
        return 0
    
    while N != 0:
        if (N % 10) & 1 == 0:
            return False
        N //= 10
    return True

def reverseNum(N):
    revNum = 0
    while N != 0:
        revNum = 10 * revNum + N % 10
        N //= 10
    return revNum
