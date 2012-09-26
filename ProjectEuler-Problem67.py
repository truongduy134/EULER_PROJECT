# Find the maximum total from top to bottom of a triangle of height H by
# starting at the top of the triangle and moving to adjacent numbers on the row.
# Note that from A[row][col], you have only 2 directions to go:
#       1) To A[row + 1][col]
#       2) To A[row + 1][col + 1]

# Note that at height h >= 1, there are exactly h elements.

myTriangle = []

def findMaxTotal():
    global myTriangle
    
    height = readTriangle()

    # Since 0-indexing, at the row K, there are (K + 1)-th columns actually!
    for row in range(1, height):
        for col in range(0, row + 1): 
            if col == 0:
                # There is only 1 direction that can reach A[row][col]:
                #   1) From A[row - 1][col]
                myTriangle[row][col] += myTriangle[row - 1][col]
            elif col == row:
                # There is only 1 direction that can reach A[row][col]:
                #   1) From A[row - 1][col - 1]
                myTriangle[row][col] += myTriangle[row - 1][col - 1]
            else:
                # There are only 2 directions that can reach A[row][col]:
                #   1) From A[row - 1][col]
                #   2) From A[row - 1][col - 1]
                temp = max(myTriangle[row - 1][col], myTriangle[row - 1][col - 1])
                myTriangle[row][col] += temp
        
    return max(myTriangle[height - 1])
            
def readTriangle():
    global myTriangle
    
    height = int(input('Enter the height of the triangle: '))

    myTriangle = [[0] * row for row in range(1, height + 1)]

    triangleText = input('Enter the triangle itself: ')
    setRow = triangleText.split('\n')

    curRow = 0
    for row in setRow:
        setNumStr = row.split(' ')

        setNum = [int(numStr) for numStr in setNumStr]

        myTriangle[curRow] = setNum
        curRow += 1

    return height
