# A number N is abundant if the sum of all its proper divisors exceeds N
# By mathematical analysis, it can be shown that all integers greater than
#   28123 can be written as the sum of two abundant numbers.
# Find the sum of all positive integers which cannot be written as the sum
#   of two adundant numbers.

from math import floor, sqrt

LIMIT = 28123

# Find the sum of all positive integers which CANNOT be written as the sum
#   of two adundant numbers.
def findSpecialSum():
    listAbundant = generateAbundantNumber()
    
    mySum = 0

    for x in range(1, LIMIT + 1):
        if not isSumOfAbundantNum(x, listAbundant):
            mySum += x

    return mySum

# Return true if N can be expressed of the sum of 2 abundant numbers
#   in listAbundant
# Note that listAbundant contains abundant numbers in ascending order
def isSumOfAbundantNum(N, listAbundant):
    if N > LIMIT:
        return True

    # Case 1: N = 2 * X where X is an abundant number
    for x in listAbundant:
        if x + x == N:
            return True

    # Case 2: N = X + Y where X, Y are 2 distinct abundant numbers
    head = 0
    tail = len(listAbundant) - 1
    while head <= tail:
        if listAbundant[head] + listAbundant[tail] == N:
            return True
        elif listAbundant[head] + listAbundant[tail] < N:
            head += 1
        else:
            tail -= 1

    return False

# Generate a list of abundant numbers whose value is at most LIMIT
def generateAbundantNumber():
    listAbundant = []
    for x in range(2, LIMIT + 1):
        if findSumProperDivisor(x) > x:
            listAbundant.append(x)

    return listAbundant

# Find the sum of proper divisors of an input number N
def findSumProperDivisor(N):
    if N <= 1:
        return 0
   
    mySum = 1
    x = 2
    upperBound = floor(sqrt(N))
    while x <= upperBound:
        if N % x == 0:
            mySum += x
            
            otherDivisor = N // x
            if otherDivisor != x:
                mySum += otherDivisor
                
        x += 1

    return mySum
            
    
