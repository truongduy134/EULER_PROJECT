# We have:
#   + Black tiles: measure 1 unit
#   + Red tiles: measure 2 units
#   + Green tiles: measure 3 units
#   + Blue tiles: measure 4 units
# Task: How many ways to tile a row with N units in length using black, red,
#           green, and blue tiles?
#
# Methodology:
#   + Define f(n) = the number of ways to tile a row with N units in length
#                   using black, red, green, and blue tiles.
#   + Recurrence relation: For n >= 4
#       f(n) = f(n - 1)         // Try using a black tile
#            + f(n - 2)         // Try using a red tile
#            + f(n - 3)         // Try using a green tile
#            + f(n - 4)         // Try using a blue tile
#   + Base cases:
#       f(0) = 1
#       f(1) = 1
#       f(2) = f(1) + f(0)
#       f(3) = f(2) + f(1) + f(0)
#
# Time complexity: O(N)
def countNumTile(N):
    if N == 0 or N == 1:
        return 1

    numTile = [0] * (N + 1)
    numTile[0] = numTile[1] = 1
    numTile[2] = numTile[1] + numTile[0]
    if N >= 3:
        numTile[3] = numTile[2] + numTile[1] + numTile[0]

        for n in range(4, N + 1):
            numTile[n] = numTile[n - 1] + numTile[n - 2] + numTile[n - 3] + numTile[n - 4]

    return numTile[N]            
