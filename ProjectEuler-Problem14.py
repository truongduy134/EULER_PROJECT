# Find the number n <= 10^6 that produces the longest Collatz sequence.

LEN = 1000000

# Declare an array such that the i-th element of the array indicates
#       the length of the Collatz sequence starting at i.
collatzLength = []

def findLongestCollatzNum():
    initializeArr()

    longestNum = 1

    for num in range(2, LEN + 1):
        if findCollatzLength(num) > findCollatzLength(longestNum):
            longestNum = num

    return longestNum

# Initialize the collatzLength array
def initializeArr():
    global collatzLength

    collatzLength = [0] * (LEN + 1)
    collatzLength[1] = 1

# Find the length of the Collatz sequence starting at N.
# Use memoization to speed up the implementation
def findCollatzLength(N):
    global collatzLength

    if N <= LEN and collatzLength[N] > 0:
        return collatzLength[N]

    length = 0
    if N % 2 == 0:
        length = 1 + findCollatzLength(N // 2)
    else:
        length = 1 + findCollatzLength(3 * N + 1)

    if N <= LEN:
        collatzLength[N] = length

    return length




