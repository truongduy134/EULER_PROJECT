# Task: Find the last ten digits of the number: 28433 * 2 ^ (7830457) + 1

# Take the last ten digits of the result of the expression
#       C * E^B + D
def takeDigitFromExpression(C, E, B, D, numDigit):
    myMod = 10 ** numDigit

    return (((C % myMod) * pow(E, B, myMod)) % myMod + D % myMod) % myMod
