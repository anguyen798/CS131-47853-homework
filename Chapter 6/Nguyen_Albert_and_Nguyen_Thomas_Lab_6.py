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

# Lab 6b
import pandas
#Tables are created with the expected output to later be used for comparison
table1 = [16, 3, 2, 13]
table2  = [5, 10, 11, 8]
table3 = [9, 6, 7, 12]
table4 = [4, 15, 14, 1]
table5 = table1 + table2 + table3 + table4

#User input is converted into a list and holds 16 values
numLst = list(int(num) for num in input("Enter the items followed by a space: ").strip().split())[:16]

#The set functions are used in conjunction with an if/else statement to evaluate each value in the list
userLst = set(numLst)
trueTable = set(table5)

if userLst == trueTable:
    #The lists are spliced to hold four values each
    numLst2 = numLst[0:4]
    numLst3 = numLst[4:8]
    numLst4 = numLst[8:12]
    numLst5 = numLst[12:16]
    #The values are then combined again
    lstFinal = [numLst2,
    numLst3,
    numLst4,
    numLst5
    ]
    #The lists are printed using the panda function to format the 4x4 table
    print((pandas.DataFrame(lstFinal)))
    print("It is a magic square")

else:
    numLst2 = numLst[0:4]
    numLst3 = numLst[4:8]
    numLst4 = numLst[8:12]
    numLst5 = numLst[12:16]
    lstFinal = [numLst2,
    numLst3,
    numLst4,
    numLst5
    ]
    print((pandas.DataFrame(lstFinal)))
    print("It is not a magic square")