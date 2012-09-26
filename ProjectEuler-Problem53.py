# Count how many values (not necessarily distinct) of nCr for 1 <= n <= 100


def countCombination(n, limit):
    # C[n][r] = nCr
    C = [[0] * (n + 1) for i in range(n + 1)]

    # Inialization
    for x in range(0, n + 1):
        C[x][0] = 1
    
    # Fill in the table from left to right, from top to bottom
    for x in range(1, n + 1):
        for y in range(1, n + 1):
           C[x][y] = C[x - 1][y - 1] + C[x - 1][y]

    count = 0
    for x in range(1, n + 1):
        for y in range(1, n + 1):
            if C[x][y] > limit:
                count += 1

    return count
