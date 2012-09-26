# Find the minimum path sum from top left to bottom right of an N x N matrix by
# only moving to the right and down.

myMatrix = []

def findMinPathSum():
    global myMatrix
    
    matrixSize = readMatrix()

    for row in range(0, matrixSize):
        for col in range(0, matrixSize):
            if row != 0 or col != 0:
                if col == 0:
                    # There is only 1 direction that can reach A[row][col]:
                    #   1) From A[row - 1][col] (i.e. going down)
                    myMatrix[row][col] += myMatrix[row - 1][col]
                elif row == 0:
                    # There is only 1 direction that can reach A[row][col]:
                    #   1) From A[row][col - 1] (i.e. going right)
                    myMatrix[row][col] += myMatrix[row][col - 1]
                else:
                    # There are only 2 directions that can reach A[row][col]:
                    #   1) From A[row - 1][col]
                    #   2) From A[row][col - 1]
                    temp = min(myMatrix[row - 1][col], myMatrix[row][col - 1])
                    myMatrix[row][col] += temp

    # The bottom right corner!    
    return myMatrix[matrixSize - 1][matrixSize - 1]
            
def readMatrix():
    global myMatrix
    
    matrixSize = int(input('Enter the order of the square matrix: '))

    myMatrix = [[0] * matrixSize for row in range(0, matrixSize)]

    matrixText = input('Enter the matrix itself: ')
    setRow = matrixText.split('\n')

    curRow = 0
    for row in setRow:
        setNumStr = row.split(',')

        setNum = [int(numStr) for numStr in setNumStr]

        myMatrix[curRow] = setNum
        curRow += 1

    return matrixSize
