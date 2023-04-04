
# Q1
def sideLengthSquare() :
    length = input("Please Enter the side length for the square: ")
    lengthInt = int(length)
    print("*" * lengthInt, "*" * lengthInt)
    for i in range(1, (lengthInt - 1)) :
        print("*" * lengthInt, end = " ")
        print("*", end="")
        print(" " * (lengthInt - 2), end="")
        print("*")
    print("*" * lengthInt, "*" * lengthInt)


# Q2
def sameItems(x,y) :
    sortedX = sorted(x)
    sortedY = sorted(y)
    listChecker = []
    for i in range(len(x)) :
        if sortedX[i] == sortedY[i] :
            listChecker.append("True")
        else:
            listChecker.append("False")
    print("For list x containing %s and list y containing %s" % (x, y))
    if len(x) != len(y):
        print("The lists are not identical")
    elif "False" in listChecker :
        print("The lists are not identical")
    else :
        print("The lists are identical")


# Q3
# a
def allSame(a, b, c) :
    if a == b and b == c and a == c :
        print("allSame of %s, %s, and %s is True" % (a, b, c))
        return True
    else :
        print("allSame of %s, %s, and %s is False" % (a, b, c))
        return False


def allSameMain() :
    allSame(1,2,3)
    allSame(3,2,1)
    allSame(1,3,2)
    allSame(2,2,2)

    
# b
def allDifferent(a, b, c) :
    if a != b and b != c and a != c :
        print("allDifferent of %s, %s, and %s is True" % (a, b, c))
        return True
    else :
        print("allDifferent of %s, %s, and %s is False" % (a, b, c))
        return False

def allDifferentMain() :
    allDifferent(1,2,3)
    allDifferent(3,2,1)
    allDifferent(1,3,2)
    allDifferent(2,2,2)


# c
def sorted_(a, b, c) :
    if a < b and b < c:
        print("sorted of %s, %s, and %s is True" % (a, b, c))
        return True
    elif a == b == c:
        print("sorted of %s, %s, and %s is True" % (a, b, c))
        return True        
    else :
        print("sorted of %s, %s, and %s is False" % (a, b, c))
        return False

def sortedMain() :
    sorted_(1,2,3)
    sorted_(3,2,1)
    sorted_(1,3,2)
    sorted_(2,2,2)


def main() :
    # Q1 Calls
    print("*" * 10, "Q1", "*" * 50)
    sideLengthSquare()
   
    # Q2 Calls
    print("*" * 10, "Q2", "*" * 50)
    # First Call
    x = [1, 4, 9, 16, 9, 7, 4, 9, 11]
    y = [11, 1, 4, 9, 16, 9, 7, 4, 9]    
    sameItems(x,y)
    y = [11, 11, 7, 9, 16, 4, 1, 4, 9]
    # Second Call
    sameItems(x,y)

    #Q3 Calls
    print("*" * 10, "Q3", "*" * 50)
    allSameMain()
    allDifferentMain()
    sortedMain()

main()

