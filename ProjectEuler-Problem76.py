# Find different ways to partition N into a sum of at least 2 positive integers

# Return the number of ways to partition N as the sum of
#   a1 + a2 + ... + ak
# where a1 >= a2 >= ... >= ak >= 1
#
# Methodology: Use dynamic programming
#   1) Define f(n, m, k) = the number of ways to partition n into k parts when
#                               the largest summand is m <= n.
#   2) Recurrence relation:
#           f(n, m, k) = sum{ f(n - i, i, k - 1) } for i = m downto 1
#   3) Base cases
#           f(0, m, 0) = 1
#           f(0, m, k) = 0 for k >= 1
#           f(n, m, 0) = 0 for n >= 1
#           
# Tim complexity: O(N^3 * K)

numPartition = []

def countPartition(N):
    numWay = 0
    
    initializeMemoTable(N, N)
    for numPartition in range(2, N + 1):
        numWay += partitionFixPart(N, N, numPartition)

    return numWay

def initializeMemoTable(N, K):
    global numPartition
    numPartition = [[[-1] * (K + 1) for i in range(N + 1)] for j in range(N + 1)]

def partitionFixPart(N, M, K):
    global numPartition
    
    if N == 0 and K == 0:
        return 1
    if N == 0 and K >= 1:
        return 0
    if N > 0 and K == 0:
        return 0

    if numPartition[N][M][K] != -1:
        return numPartition[N][M][K]

    numWay = 0
    for i in range(M, 0, -1):
        numWay += partitionFixPart(N - i, min(i, N - i), K - 1)
    numPartition[N][M][K] = numWay

    return numWay
    
