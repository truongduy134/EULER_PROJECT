def DigitSumOfExponential(B, E):
    exponential = B**E
    digitSum = 0
    while exponential > 0:
        digitSum += exponential % 10
        exponential //= 10
    return digitSum
