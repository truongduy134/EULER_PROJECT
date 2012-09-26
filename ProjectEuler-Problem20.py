def DigitSumOfFactorial(N):
    factorial = 1
    digitSum = 0
    for i in range(2, N):
        factorial *= i
    while factorial > 0:
        digitSum += factorial % 10
        factorial //= 10
    return digitSum
