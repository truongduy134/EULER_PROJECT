# Find the first term in the Fibonacci sequence that contains 1000 digits
# F(1) = 1, F(2) = 1, F(3) = 2, ...

from math import log10, floor, ceil

def FindIndexOfFirstFiboTermWithNDigit(N):
    if N == 1:
        return 1
    pre = 1
    curr = 1
    termIndex = 2
    while (floor(log10(curr)) + 1) != N:
        temp = curr
        curr += pre
        pre = temp
        termIndex += 1
    return termIndex
