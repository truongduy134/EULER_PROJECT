# totient(n) = the Euler's Totient function evaluated at n.

# Define ratio(n) = n / totient(n).
# We want to find n <= 10^6 such that n / totient(n) is maximum.

# Mathematical result:
#   totient(n) = n * product(1 - 1 / p) for all distinct primes p that divide n.
# Hence, we have:
#   ratio(n) = n / totient(n) = 1 / product(1 - 1 / p)
#                             = product(p / (p - 1))
#   for all distinct primes p that divide n.

LIMIT = 1000000

# Find the number n <= 10^6 such that ratio(n) is maximum
def findMaxRatio():
    ratio = computeRatio()

    maxN = 1
    for n in range(2, LIMIT + 1):
        if ratio[n] > ratio[maxN]:
            maxN = n

    return maxN

# Compute ratio(n) for all n <= LIMIT
# Note that totient(1) = 1
def computeRatio():
    ratio = [0] * (LIMIT + 1)
    # ratio[0] is a dummy value

    ratio[1] = 1
    
    for n in range(2, LIMIT + 1):
        if ratio[n] == 0:       # n is a prime
            multiple = n
            term = n / (n - 1)
            
            while multiple <= LIMIT:
                if ratio[multiple] == 0:
                    ratio[multiple] = 1
                ratio[multiple] *= term
                multiple += n

    return ratio
