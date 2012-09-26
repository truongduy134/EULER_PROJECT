# Find the first 4 consecutive integers (A, A + 1, A + 2, A + 3)that
# have four distinct prime factors.
# Output A

def findSpecialNumber():
    targetNumFactor = 4
    targetNumConsecutive = 4
    listPrime = []

    x = 2
    numConsecutive = 0
    while True:
        (numFactor, isPrime) = countPrimeFactor(x, listPrime)
       
        if numFactor == targetNumFactor:
            numConsecutive += 1
        else:
            # Reset the counter
            numConsecutive = 0

            if isPrime:
                listPrime.append(x)
                
        if numConsecutive == targetNumConsecutive:
            return x - targetNumConsecutive + 1

        x += 1
    
        
def countPrimeFactor(N, listPrime):
    if N <= 1:
        return 0

    numPrimeFactor = 0
    isPrime = False
    
    index = 0
    lenList = len(listPrime)

    while index < lenList and listPrime[index] <= N:
        if N % listPrime[index] == 0:
            numPrimeFactor += 1
           
            while N % listPrime[index] == 0:
                N = N // listPrime[index]
                    
        index += 1

    if numPrimeFactor == 0:        # So N is a prime
        isPrime = True
        
    return (numPrimeFactor, isPrime)


