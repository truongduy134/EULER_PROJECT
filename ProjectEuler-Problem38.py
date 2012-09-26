# A number is called 1 to 9 pandigital 9-digit if it is a permutation of
#   the digits 1, 2, ..., 9
#
# Find the largest 1 to 9 pandigital 9-digit number that can be formed as
# the concatenated product of an integer with (1,2, ... , n) where n > 1
#
# When n = 9: we have 123456789
#
# After some calculation, we know that n != 8 and n != 7

def test():
    result = 0
    for x in range(5000, 10000):
        y = x * (10 ** 5) + 2 * x
        if isPandigital(y):
            result = max(result, y)
    return result

def isPandigital(N):
    sieve = [0] * 10

    while N != 0:
        sieve[N % 10] += 1
        N //= 10

    if sieve[0] != 0:
        return False
    for index in range(1, 10):
        if sieve[index] != 1:
            return False
    return True
