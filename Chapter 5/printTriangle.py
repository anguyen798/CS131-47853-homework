def printTriangle(sideLength) :
    if sideLength < 1 : return
    printTriangle(sideLength - 1)
    print("[]" * sideLength)

printTriangle(4)