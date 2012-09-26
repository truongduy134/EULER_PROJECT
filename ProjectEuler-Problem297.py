
globalFiboArr = []
sizeFiboArr = 0
zeckendorfFibo = []

def mainComputeZeck(upperLimit):
    generateFibo(upperLimit)
    computeZeckForFibo()
    
    return computeZeck(upperLimit - 1)
    
def computeZeck(num):
    if num == 0:
        return 0

    index = findClosetFibo(num)

    return zeckendorfFibo[index] + num - globalFiboArr[index] + computeZeck(num - globalFiboArr[index])
# Compute s(n) = 
def computeZeckForFibo():
    global zeckendorfFibo

    zeckendorfFibo = [0] * sizeFiboArr
    zeckendorfFibo[0] = 1
    zeckendorfFibo[1] = 2
    
    for index in range(2, sizeFiboArr):
        zeckendorfFibo[index] = zeckendorfFibo[index - 1] + zeckendorfFibo[index - 2] + globalFiboArr[index - 2] - 1
        
    
# Generate Fibonacci numbers (starting from 1, 2) that are less than LIMIT
def generateFibo(limit):
    global globalFiboArr, sizeFiboArr
    
    globalFiboArr = [1, 2]
    curIndex = 1

    while True:
        nextFibo = globalFiboArr[curIndex] + globalFiboArr[curIndex - 1]

        if nextFibo >= limit:
            break

        globalFiboArr.append(nextFibo)
        curIndex += 1

    sizeFiboArr = len(globalFiboArr)

# Find the index of the largest Fibonacci number in the global arr
#   globalFiboArr that is less than or equal to num
def findClosetFibo(num):
    for index in range(0, sizeFiboArr - 1):
        if globalFiboArr[index] <= num and globalFiboArr[index + 1] > num:
            return index

    return sizeFiboArr - 1
