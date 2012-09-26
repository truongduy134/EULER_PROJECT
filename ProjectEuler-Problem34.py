# Find sum of all numbers which are equal to the sum of the factorial of their
# digits.

factorialDigit = []

def computeFactorialDigit():
    global factorialDigit

    factorialDigit.append(1)    # 0!
    factorialDigit.append(1)    # 1!
    for x in range(2, 10):
        factorialDigit.append(x * factorialDigit[x - 1])
        
def computeFactorialSumDigit(N):
    if N <= 0:
        return 1

    mySum = 0
    while N != 0:
        mySum += factorialDigit[N % 10]
        N = N // 10

    return mySum

# Find sum of all numbers which are equal to the sum of the factorial of their
# digits.

# Note that if N is the sum of the factorial of its digits, then 10 <= N < 10^7
def computeSumSpecialNum():
    
    computeFactorialDigit()
    
    mySum = 0

    limit = 10**7
    for x in range(10, limit):
        if computeFactorialSumDigit(x) == x:
            mySum += x

    return mySum
