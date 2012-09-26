# Let us denote A -> B as the process where B is obtained by summing all
#       the factorial of the digits of A.
# We have:
#   145 -> 145
#   169 -> ... -> 169
#   871 -> ... -> 871
#   872 -> ... -> 872
#
# For a natural number A, we denote NonRepeatTerm(A) to be the number of
#   non-repeating terms in the chain A -> ... -> ...
# We have:
#   NonRepeatTerm(145)= 1
#   NonRepeatTerm(169) = NonRepeatTerm(36301) = NonRepeatTerm(1454) = 3
#   NonRepeatTerm(871) = NonRepeatTerm(45361) = 2
#   NonRepeatTerm(872) = NonRepeatTerm(45362) = 2
#   NonRepeatTerm(1) = NonRepeatTerm(0) = NonRepeatTerm(2) = 1 trivially
#
# TASK: Count the number of chains, with a starting number below 10^6,
#   contains exactly 60 non-repeating terms.
#
# Note that only 0, 1, 2, 145, 169, 871, 872, 36301, 1454, 45361, 45362 have
#   the loop properties.

FACTORIAL_DIGIT = []
LIMIT = 1000000
RECURSE_LIMIT = 80

# Global sieve for memoization purposes.
NonRepeatTerm = []

# Count numbers X such that NonRepeatTerm(X) = L where L is the specified input.
# Assumption: L < RECURSE_LIMIT
def countChain(L):
    # Pre-processing
    preComputeFactorialDigit()
    computeNonRepeatTerm()

    # Counting!
    count = 0
    for n in range(0, LIMIT):
        if NonRepeatTerm[n] == L:
            count += 1

    return count

# Compute min(NonRepeatTerm(N), RECURSE_LIMIT) for all N < LIMIT
def computeNonRepeatTerm():
    global NonRepeatTerm

    NonRepeatTerm = [0] * LIMIT

    # Initialize the array with some special numbers N (that result in a loop
    # in the chain N -> ... -> ...)
    NonRepeatTerm[0] = NonRepeatTerm[1] = NonRepeatTerm[2] = 1
    NonRepeatTerm[145] = 1
    NonRepeatTerm[169] = NonRepeatTerm[36301] = NonRepeatTerm[1454] = 3
    NonRepeatTerm[871] = NonRepeatTerm[45361] = 2
    NonRepeatTerm[872] = NonRepeatTerm[45362] = 2

    for n in range(0, LIMIT):
        if NonRepeatTerm[n] == 0:
            countNumNonRepeatTerm(n, 1)

# Compute min(NonRepeatTerm(N), RECURSE_LIMIT) for a specific N
# When the number of recursion levels exceeds RECURSE_LIMIT, we return
#       RECURSE_LIMIT
def countNumNonRepeatTerm(N, recurseLevel):
    global NonRepeatTerm

    if recurseLevel > RECURSE_LIMIT:
        return RECURSE_LIMIT
    
    if N < LIMIT and NonRepeatTerm[N] != 0:
        return NonRepeatTerm[N]

    # When reaching here, N is not special (i.e. it does not generate a loop
    #   to itself in the chain N -> ... -> ...). Therefore, we have:
    #       NonRepeatTerm(N) = 1 + NonRepeatTerm(X) where X is obtained by
    #   summing factorials of all the digits of N.
    resutl = 0
    nextResult =  countNumNonRepeatTerm(sumFactorialDigit(N), recurseLevel + 1)
    if nextResult == RECURSE_LIMIT:
        result = RECURSE_LIMIT
    else:
        result = 1 + nextResult
        
    if N < LIMIT:
        NonRepeatTerm[N] = result

    return result
    
# Pre-compute factorial of digits 0, 1, ..., 9
def preComputeFactorialDigit():
    global FACTORIAL_DIGIT
    
    FACTORIAL_DIGIT = [1]*10

    for n in range(2, 10):
        FACTORIAL_DIGIT[n] = n * FACTORIAL_DIGIT[n - 1]

# Compute the sum
def sumFactorialDigit(N):
    mySum = 0

    while N != 0:
        mySum += FACTORIAL_DIGIT[N % 10]
        N //= 10

    return mySum
