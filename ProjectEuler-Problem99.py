# Given an array of length N whose each element is a tuple (base, exponent),
# find the position in the array (1-indexing) such that base ^ exponent
# is largest!

# Methodology: A ^ B > C ^ D iff B * ln(A) > D * ln(C)

from math import *

def findMaxExpoValue():
    arrInput = readInputFromFile()

    arrLen = len(arrInput)

    maxIndex = 0
    # For each arrInput[I], we have:
    #   arrInput[I][0] contains the base
    #   arrInput[I][1] contains the exponent
    for index in range(1, arrLen):
        curValue = arrInput[index][1] * log(arrInput[index][0])
        curMaxValue = arrInput[maxIndex][1] * log(arrInput[maxIndex][0])

        if curValue > curMaxValue:
            maxIndex = index

    # The final result must be 1-indexing!
    return maxIndex + 1
    
def readInputFromFile():
    strFile = input('Enter the path of the input file: ')
    file = open(strFile, 'r')

    arrInput = []
    for line in file:
        twoNum = line.split(',')
        arrInput.append((int(twoNum[0]), int(twoNum[1])))

    return arrInput
