# Description:
#   + Read a list of integers from the user.
#   + Find the first ten digits of the sum of the input numbers

NUM_TAKEN_DIGIT = 10

def computeSum():
    arrInput = []

    strInput = input()

    arrStrNum = strInput.split('\n')
    
    for strNum in arrStrNum:
        arrInput.append(int(strNum))

    if not any(arrInput):
        return

    mySum = arrInput[0]
    length = len(arrInput)
    for index in range(1, length):
        mySum += arrInput[index]

    strSum = str(mySum)

    print(strSum[:NUM_TAKEN_DIGIT])
