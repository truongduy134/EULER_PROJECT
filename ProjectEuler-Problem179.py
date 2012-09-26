# Find the number of integers 1 < N < 10^7, for which N and N + 1 have the same
# number of positive divisors!

numDivisorSieve = []

# Count the number of integer 1 < N < limit such that N and N + 1 have the
# same divisors
def countConsecutiveSameNumDivisor(limit):
    countNumDivisorSieve(limit)

    count = 0
    
    for n in range(3, limit):
        if numDivisorSieve[n] == numDivisorSieve[n - 1]:
            count += 1

    return count

# Count the number of divisors of N for 1 < N < limit
# Methodology: Modify the Sieve of Eratosthenes Algorithm
# Time complexity: O(N * log N) where N is the length of the sieve!
def countNumDivisorSieve(limit):
    global numDivisorSieve

    # Every positive integer has at least 1 divisor (1 is a divisor of every
    # positive integer!)
    numDivisorSieve = [1] * limit

    for n in range(2, limit):
        multiple = n

        while multiple < limit:
            # n is a positive divisor of multiple!
            numDivisorSieve[multiple] += 1
            multiple += n
    
    
