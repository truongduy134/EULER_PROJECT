# Considering natural numbers of the form a^b (a, b < 100), what is the maximum
# digital sum?

# Find the maximal digital sum of numbers of the form a^b where (0 < a, b < N)
def findMaxDigitSum(limit):
    maxSum = 0
    for a in range(1, limit):
        for b in range(1, limit):
            mySum = computeDigitSum(fastExponential(a, b))

            if mySum > maxSum:
                maxSum = mySum

    return maxSum

def fastExponential(A, B):
    if B == 0:
        return 1

    if B % 2 == 0:
        temp = fastExponential(A, B // 2)
        return temp * temp
    else:
        return A * fastExponential(A, B - 1)
    
def computeDigitSum(N):
    mySum = 0

    while N != 0:
        mySum += N % 10
        N //= 10

    return mySum
