# Lab 8a
def listUnionAB(listA, listB) :
    listUnion = []
    for elementA in listA:
        if elementA not in listUnion :
            listUnion.append(elementA)
    for elementB in listB :
        if elementB not in listUnion :
            listUnion.append(elementB)
    print("List A is %s" % listA)
    print("List B is %s" % listB)
    print("The union of two lists is %s" % listUnion)


# include below in def main() and call main():
# Lab 8a

def main() :
    listA = [1, 5, 6, 8, 5]
    listB = [3, 4, 1, 5, 1, 7]
    listUnionAB(listA, listB)
    
    listA = ['red', 'white', 'red']
    listB = ['green', 'white', 'yellow']
    listUnionAB(listA, listB)

# Lab 8b

# Lab 8c
import lab8C
string = "John Wick"
lab8C.is_uniques(string)
string = "Samantha Ahtnamas"
lab8C.is_uniques(string)
string = "The quick brown fox jumps over the lazy dog"
lab8C.is_pangram(string)
string = "The slow brown wolf jumps over the energetic coyote"
lab8C.is_pangram(string)
# Lab 8d