# Read an n-digit number from the user (n >= 5)
# Find the greatest product of five consecutive digits in that number

MAX_LEN = 5

def computeGreatestProduct():
    num = input("Enter number: ")

    length = len(num)
    
    # Note that we can skip considering sequences that contains zero!
    maxProduct = 0

    curLen = 0
    index = 0

    while index < length:
        newDigit = ord(num[index]) - ord('0')

        if newDigit == 0:
            # Ignore all sequences of length MAX_LEN that are through this
            # element since they are zero anyway
            curLen = 0
        else:
            # The case newDigit != 0

            # Loop invariant:
            #   + At the beginning of this loop, if curLen > 0, the sequence
            #       (A[index - curLen + 1], ..., A[index]) contains non-zero
            #       elements.
            #
            #   + At the end of this loop, if A[index] != 0, product is the
            #       value of the product of elements in the sequence
            #       (A[index - curLen + 1], ..., A[index])
            if curLen == 0:
                product = newDigit
                curLen += 1
            elif curLen < MAX_LEN:
                    product *= newDigit
                    curLen += 1

            else:
                # The case curLen == MAX_LEN
                headSequence = ord(num[index - curLen + 1]) - ord('0')
                product = (product // headSequence) * newDigit

        if curLen == MAX_LEN and product > maxProduct:
            maxProduct = product
            
        index += 1
    
    print(maxProduct)
    
    

    
