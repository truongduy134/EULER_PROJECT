# Find the last ten digits of the series 1^1 + 2^2 + 3^3 + ... + N^N

def findDigitSumSeries(N, numDigit):
    division = fastExponential(10, numDigit)

    seriesDigit = 0
    for x in range(1, N + 1):
        seriesDigit = (seriesDigit + fastExponential(x, x)) % division

    return seriesDigit

def fastExponential(base, power):
    if power <= 0:
        return 1
    if power == 1:
        return base

    if power % 2 == 0:
        temp = fastExponential(base, power // 2)
        return temp * temp
    else:
        return base * fastExponential(base, power - 1)
        
