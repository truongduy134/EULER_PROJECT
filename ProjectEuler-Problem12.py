# Find the first triangle number that has over 500 divisors.

def findNumDivisor(N):
    numDivisor = 2

    if N == 1:
        numDivisor = 1
        
    k = 2
    while k * k < N:
        if N % k == 0:
            numDivisor += 2
        k += 1
    if k * k == N and N % k == 0:
        numDivisor += 1
    return numDivisor

# The function finds the first triangle number that has over N divisors
def findTriangleNum(N):
    triNo = 1
    counter = 2
    
    while findNumDivisor(triNo) <= N:
        triNo += counter
        counter += 1

    return triNo
