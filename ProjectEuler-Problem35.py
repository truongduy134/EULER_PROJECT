# The number, 197, is called a circular prime because all rotations of the
# digits: 197, 971, and 719, are themselves prime.

# 1-digit primes are circular

# Find the number of circular primes below 10^6

LIMIT = 10**6

# Testing
def test():
    (listPrime, sieve) = generatePrimes()
    for x in range(0, 10):
        print(listPrime[x])

# Find the number of circular primes below LIMIT
def countCircularPrime():
    (listPrime, primeSieve) = generatePrimes()

    numCircular = 0

    for prime in listPrime:
        if isCircularPrime(prime, primeSieve):
            numCircular += 1
            
    return numCircular

def isCircularPrime(prime, primeSieve):
    # If input is a composite, not a prime
    if primeSieve[prime] == 1:
        return False

    numDigit = findNumDigit(prime)
    # Only need to rotate (numDigit - 1) times.
    rotate = prime
    for time in range(1, numDigit):
        rotate = leftRotate(rotate, numDigit)
        if primeSieve[rotate] == 1:
            return False

    return True

# Generate the list of primes below LIMIT using Sieve of Eratosthenes algorithm
def generatePrimes():
    # Declare a sieve of 10^6 elements. All is initialized to 0
    sieve = [0] * LIMIT

    sieve[0] = 1
    sieve[1] = 1

    for x in range(2, LIMIT):
        if sieve[x] == 0:       # x is a prime
            multiple = 2
            while multiple * x < LIMIT:
                sieve[multiple * x] = 1
                multiple += 1

    # Go through the sieve and filter the primes
    listPrime = []
    for x in range(2, LIMIT):
        if sieve[x] == 0:
            listPrime.append(x)

    return (listPrime, sieve)

# Rotate a number N with numDigit digits to the left.
# For example: 964 -> 649
def leftRotate(N, numDigit):
    powerTen = 10 ** (numDigit - 1)
    
    leadDigit = N // powerTen

    return (N % powerTen) * 10 + leadDigit

# Return the number of digits in the decimal representation of an input number N
def findNumDigit(N):
    if N == 0:
        return 1

    numDigit = 0
    while N != 0:
        numDigit += 1
        N //= 10

    return numDigit

