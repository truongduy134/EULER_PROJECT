# A number that never forms a palindrome through the reverse and add process
# is called a Lychrel number.

# For every number below ten-thousand, it will either
#    (i) become a palindrome in less than fifty iterations, or,
#   (ii) no one, with all the computing power that exists, has managed so
#           far to map it to a palindrome.

# Find the number of Lychrel numbers below ten thousand.

LIMIT = 10**4
MAX_ITERATION = 50

def countLychrelNum():
    count = 0
    for x in range(1, LIMIT):
        if isLychrelNum(x):
            count += 1

    return count

# Return true if N is a Lychrel number.
# Pre-condition: N is a positive integer below ten thousand
def isLychrelNum(N):
    for time in range(0, MAX_ITERATION):
        N += reverseNum(N)

        if isPalindrome(N):
            return False

    return True

# Return the number formed by reversing the digits of the input number N.
def reverseNum(N):
    reverse = 0

    while N != 0:
        reverse = 10 * reverse + N % 10
        N //= 10

    return reverse

# Return true if the decimal representation of N is a palindrome
def isPalindrome(N):
     reverse = reverseNum(N)

     if reverse == N:
         return True
    
     return False


    
