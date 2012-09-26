# You are given a file containing the coordinates in 2D plane of 3 points of
# N triangles (line by line, comma-seperated in each line).
#
# Task: Count the number of triangles that contain the origin.

MAX_LEN = 3
MAX_NUM = 6

def countNumTriangleContainOrigin():
    fileName = input('Enter the name of the file: ')

    inputFile = open(fileName, 'r')

    count = 0

    pointOrigin = Point3D([])
    
    for line in inputFile:
        arrStrNum = line.split(',')

        # Find the coordinates of the 3 points A, B, C of a triangle
        pointA = Point3D([int(arrStrNum[0]), int(arrStrNum[1])])
        pointB = Point3D([int(arrStrNum[2]), int(arrStrNum[3])])
        pointC = Point3D([int(arrStrNum[4]), int(arrStrNum[5])])

        if containPoint(pointA, pointB, pointC, pointOrigin):
            count += 1

    return count

# Return True if the triangle ABC contains the point D. Return False otherwise
def containPoint(pointA, pointB, pointC, pointD):
    if isOnSameSide(pointA, pointB, pointC, pointD) and isOnSameSide(pointB, pointC, pointA, pointD) and isOnSameSide(pointA, pointC, pointB, pointD):
        return True

    return False

# Return True if point C and point D are on the same side relative to
#   the straight line AB
# Return False otherwise
def isOnSameSide(pointA, pointB, pointC, pointD):
    AB = Vector3D([pointA, pointB])
    AC = Vector3D([pointA, pointC])
    AD = Vector3D([pointA, pointD])

    crossOne = AB.crossProduct(AC)
    crossTwo = AB.crossProduct(AD)

    if crossOne.dotProduct(crossTwo) >= 0:
        return True

    return False

class Point3D:
    # Constructor
    def __init__(self, inputTuple):
        # Note that we only care the first 3 numbers in the tuple!
        myLen = min(MAX_LEN, len(inputTuple))

        self.coordArr = [0] * MAX_LEN
        for index in range(0, myLen):
            self.coordArr[index] = inputTuple[index]

    def __repr__(self):
        return "Point3D(%s, %s, %s)" % (self.coordArr[0], self.coordArr[1], self.coordArr[2])

    def __str__(self):
        return "(%f, %f, %f)" % (self.coordArr[0], self.coordArr[1], self.coordArr[2])
    

class Vector3D:
    # Constructor
    def __init__(self, listPoint):
        numElement = len(listPoint)

        if numElement == 0:
            # Case 1: listPoint is empty. Then we create a zero vector
            self.coordArr = [0] * MAX_LEN
        elif numElement == 1:
            # Case 2: there is 1 point A. Then we create the vector OA
            if not isinstance(listPoint[0], Point3D):
                raise TypeError(listPoint[0] + ' is not a Point3D object!')
            self.coordArr = [0] * MAX_LEN
            for index in range(0, MAX_LEN):
                self.coordArr[index] = listPoint[0].coordArr[index]
        else:
            # Case 3: there are 2 points A and B. Then we create the vector AB
            for index in range(0, 2):
                if not isinstance(listPoint[index], Point3D):
                    raise TypeError(listPoint[index] + ' is not a Point3D object!')

            self.coordArr = [0] * MAX_LEN
            for index in range(0, MAX_LEN):
                self.coordArr[index] = listPoint[1].coordArr[index] - listPoint[0].coordArr[index]

    def __repr__(self):
        return "Vector3D(%s, %s, %s)" % (self.coordArr[0], self.coordArr[1], self.coordArr[2])

    def __str__(self):
        return "(%f, %f, %f)" % (self.coordArr[0], self.coordArr[1], self.coordArr[2])

    # Compute the sum of 2 vectors
    def __add__(self, other):
        sumVector = Vector3D([])

        for index in range(0, MAX_LEN):
            sumVector.coordArr[index] = self.coordArr[index] + other.coordArr[index]

        return sumVector
    
    # Compute the dot product of this vector and otherVector
    def dotProduct(self, otherVector):
        mySum = 0
        for index in range(0, MAX_LEN):
            mySum += self.coordArr[index] * otherVector.coordArr[index]
        return mySum

    # Compute the cross product of this vector and otherVector in 3D
    # This is only applicable to 3D vectors
    def crossProduct(self, otherVector):
        crossVector = Vector3D([])

        for index in range(0, MAX_LEN):
            crossVector.coordArr[index] = self.coordArr[(index + 1) % 3] * otherVector.coordArr[(index + 2) % 3] - self.coordArr[(index + 2) % 3] * otherVector.coordArr[(index + 1) % 3]

        return crossVector

    
