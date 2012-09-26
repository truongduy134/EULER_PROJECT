# The radical of n, rad(n), is the product of distinct prime factors of n.

# Let A(n) be the sorted array of rad(i) for 1 <= i <= n.
# Let E(k) be the corrsponding M of the value rad(M) at the index k in A(n)

# Task: find E(10000) for n = 100000

from operator import itemgetter

radicalSieve = []

def findElementAtIndex(K, N):
    global radicalSieve
    
    computeRadicalSieve(N)

    # Note that sorting in Python is stable!
    radicalSieve = sorted(radicalSieve, key = itemgetter(1), reverse = False)

    # By specification, A(n) starts with (1, A(1)) while radicalSieve starts with
    # the dummy value (0, 1). But this does not affect the result since
    # array in Python is 0-indexing!
    return radicalSieve[K][0]

# radicalSieve[n] is a pair of integers (n, rad(n)) for n >= 2
def computeRadicalSieve(upperBound):
    global radicalSieve
    
    radicalSieve = [(1, 1)] * (upperBound + 1)

    for n in range(2, upperBound + 1):
        if radicalSieve[n][1] == 1:
            # n is a prime!
            multiple = n

            while multiple <= upperBound:
                curValue = radicalSieve[multiple][1]
                radicalSieve[multiple] = (multiple, curValue * n)
                multiple += n
    
    
    
    
