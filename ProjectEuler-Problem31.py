# DENOM = [1, 2, 5, 10, 20, 50, 100, 200] be the list of denominations in
# ascending order.
#
# Let numExchange(N, i) = the number of ways to exchange N pences and the largest
#   denomination we can use is DENOM[i]
#
# Recurrence relation:
# Then numExchange(N) = sum(numExchange(N - DENOM[j], j)) for 0 <= j <= i and
#           DENOM[j] <= N
#
# Base cases:
#   numExchange(0, K) = 1 for all K
#
# Methodology: Using dynamic programming!

DENOM = [1, 2, 5, 10, 20, 50, 100, 200]
NUM_DENOM = 8

def countNumExchange(N):
    if N < 0:
        return 0
    
    numExchange = [[0] * NUM_DENOM for row in range(0, N + 1)]

    for denomIndex in range(0, NUM_DENOM):
        numExchange[0][denomIndex] = 1
    
    for n in range(1, N + 1):
        for denomIndex in range(0, NUM_DENOM):
            for nextDenom in range(0, denomIndex + 1):   
                if n - DENOM[nextDenom] >= 0:
                    numExchange[n][denomIndex] += numExchange[n - DENOM[nextDenom]][nextDenom]

    return numExchange[N][NUM_DENOM - 1]

    
