# Find the maximum product of 4 adjacent numbers horizontally, vertically
# and diagonally (2 directions) in a matrix of size n x n


myMatrix = []

def findMaxProduct():
    sizeMatrix = readMatrix()

    maxProduct = 0
    for row in range(0, sizeMatrix):
        for col in range(0, sizeMatrix):
            maxProduct = max(maxProduct, findMaxProductAt(row, col, sizeMatrix))

    return maxProduct

# Find the maximum product of 4 adjancy elements starting at myMatrix(row, col)
# in the directions from left to right, from top to bottom, and along the
# 2 digonals downwards!
def findMaxProductAt(row, col, sizeMatrix):
    maxProduct = 0

    # Top to bottom
    verProduct = myMatrix[row][col]
    for xCoord in range(row + 1, row + 4):
        if xCoord >= sizeMatrix:
            verProduct = 0
            break
        verProduct *= myMatrix[xCoord][col]
    maxProduct = max(maxProduct, verProduct)

    # Left to right
    horProduct = myMatrix[row][col]
    for yCoord in range(col + 1, col + 4):
        if yCoord >= sizeMatrix:
            horProduct = 0
            break
        horProduct *= myMatrix[row][yCoord]
    maxProduct = max(maxProduct, horProduct)

    # The digonal from left to right, from top to bottom
    lDiagProduct = myMatrix[row][col]
    for incre in range(1, 4):
        if row + incre >= sizeMatrix or col + incre >= sizeMatrix:
            lDiagProduct = 0
            break
        lDiagProduct *= myMatrix[row + incre][col + incre]
    maxProduct = max(maxProduct, lDiagProduct)

    # The digonal from right to left, from top to bottom
    rDiagProduct = myMatrix[row][col]
    for x in range(1, 4):
        if row - x < 0 or col + x >= sizeMatrix:
            rDiagProduct = 0
            break
        rDiagProduct *= myMatrix[row - x][col + x]
    maxProduct = max(maxProduct, rDiagProduct)

    return maxProduct
                            
def readMatrix():
    global myMatrix
    
    sizeMatrixStr = input('Enter the size of a matrix: ')
    sizeMatrix = int(sizeMatrixStr)
    
    myMatrix = [[0] * sizeMatrix for row in range(0, sizeMatrix)]
    
    matrixText = input('Enter the matrix: ')
    setRow = matrixText.split('\n')

    curRow = 0
    for row in setRow:
        setElementStr = row.split(' ')

        setElementNum = [int(strNum) for strNum in setElementStr]

        myMatrix[curRow] = setElementNum
        curRow += 1

    return sizeMatrix
