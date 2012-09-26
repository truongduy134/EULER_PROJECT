# Let S be a list of permutations of 0, 1, 2, ..., 9 which are sorted in
#   ascending order.
# Find S[10^6]

# Define permu(n, D) = S[n] which is the n-th permutation in S where D is
#           the set of possible digits.
#
# Let M = |D|
# permu(n, D) = 'i' + permu(n - (M! - (M + 1)!), D\{i})
#   for k <= i in S where i is in S such that max(0, (i - 1)!) <= n <=  i! 
factorialArr = []

def precalculateFactorial():
    global factorialArr

    factorialArr = [1] * 10
    for n in range(2, 10):
        factorialArr[n] = n * factorialArr[n - 1]

# Find the N-th permutation in S (N >= 1)
def findPermutation(N):
    precalculateFactorial()
    
    if N > 10 * factorialArr[9]:
        return 'Invalid input'
    
    D = [i for i in range(10)]
    return recursiveFindPermu(N, D)

def recursiveFindPermu(N, D):
    length = len(D)
    
    if N == 0:
        return ''

    index = 0
    order = 1

    myStr = ''
    while index < length and (order - 1) * factorialArr[length - 1] < N:
        if order * factorialArr[length - 1] >= N:
            myStr = str(D[index])
            D.remove(D[index])
            myStr += recursiveFindPermu(N - (order - 1) * factorialArr[length - 1], D)
        index += 1
        order += 1

    return myStr
