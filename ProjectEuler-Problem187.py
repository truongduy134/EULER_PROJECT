# Find the number of composite integers, n < 10^8, that have precisely two,
# not necessarily distinct, prime factors.

from math import floor, sqrt

LIMIT = 100000000

# A semiprime is a composite number that has precisely two, not necessarily
# distinct prime factors.
def countSemiPrime():
    numPrimeFactorSieve = findNumPrimeFactor()

    numSemi = 0

    for n in range(2, LIMIT):
        if numPrimeFactorSieve[n] == 2:
            numSemi += 1

    return numSemi

# Let f(n) be the number of prime factors (not necessarily distinct) of all integers
# 0 <= n < 10^8.
# We find min(f(n), 3) for each 0 <= n < 10^8.
# Methodology: Modify Sieve of Eratosthenes Algorithm.
def findNumPrimeFactor():
    numPrimeFactorSieve = [0]*LIMIT

    squareLimit = floor(sqrt(LIMIT))
    cubeLimit = floor(LIMIT ** (1/3))
    
    for n in range(2, LIMIT):
        if numPrimeFactorSieve[n] == 0:
            nextNum = n

            powerTwo = 0
            powerThree = 0
            if n < squareLimit:
                powerTwo = n * n
            if n < cubeLimit:
                powerThree = powerTwo * n

            while nextNum < LIMIT:
                if numPrimeFactorSieve[nextNum] <= 2:
                    if powerThree != 0 and nextNum % powerThree == 0:
                        numPrimeFactorSieve[nextNum] += 3
                    elif powerTwo != 0 and nextNum % powerTwo == 0:
                        numPrimeFactorSieve[nextNum] += 2
                    else:
                        numPrimeFactorSieve[nextNum] += 1
                nextNum += n
            
    return numPrimeFactorSieve


        
