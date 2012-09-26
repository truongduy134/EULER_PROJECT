# Find the sum of all numbers M, less than 10^6, which are palindromic
# in base 10 and base 2

LIMIT = 10**6

def findSumPalindrome():
    mySum = 0
    for x in range(1, LIMIT):
        # If x is palindromic in base 10
        if reverseNum(x, 10) == x:
            binaryString = getBinaryRepresentation(x)
            if binaryString == reverseString(binaryString):
                mySum += x

    return mySum

# Reverse the representation of a number N in base B 
def reverseNum(N, B):
    reverse = 0

    while N != 0:
        reverse = 10 * reverse + N % B
        N //= 10

    return reverse

# Return the binary representation of a decimal number N
def getBinaryRepresentation(N):
    if N == 0:
        return str(0)

    represent = ''
    while N != 0:
        represent = str(N % 2) + represent
        N //= 2

    return represent

def reverseString(S):
    return S[::-1]

    
