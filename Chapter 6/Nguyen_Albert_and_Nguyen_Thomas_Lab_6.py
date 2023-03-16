# Lab 6a

def main6a() :
    listA = [1, 4, 9, 16, 9, 7, 4, 9, 11]
    listB = [11, 1, 4, 9, 16, 9, 7, 4, 9]
    sameElements(listA, listB)
    print("*" * 50)
    listB = [11, 11, 7, 9, 16, 4, 1, 4, 9]
    sameElements(listA, listB)


def sameElements(a,b) :
    print("List 1 is", a)
    print("List 2 is", b)  
    if len(a) != len(b) :
        listIdentical = False
        print("The two lists are different sizes: List 1 has a length of %d " \
        "while List 2 has a length of %s" % (len(a), len(b)))
        return listIdentical
    indexCount = []
    for index in range(len(a)) :
        countA = a.count(a[index])
        countB = b.count(a[index])
        if countA == countB :
            indexCount.append(True)
        else :
            indexCount.append(False)
    if False in indexCount :
        listIdentical = False
    else:
        listIdentical = True
    print("The list contain the same elements: %s" % listIdentical)
    return listIdentical
      
    
main6a()