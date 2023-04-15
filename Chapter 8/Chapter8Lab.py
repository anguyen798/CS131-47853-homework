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
def intersections(dataType) :
    dataType.lower()
    #The definition checks for data types based on whether it is a string, integer or float
    if dataType == "float" :
        # If the float value is selected the user input is stored in two lists
        myList = list(map(float, input("Enter elements in the list: ").strip().split()))
        myList2 = list(map(float, input("Enter elements for the next list: ").strip().split()))
        # A variable holds the duplicate values through the set and intersection functions being used
        # Which then is returned as a list
        dupes = list(set(myList).intersection(myList2))
        print("List A is: ", myList)
        print("List B is: ", myList2)
        print("The intersection is ", dupes)
    if dataType == "string" :
        myList = list(map(str, input("Enter elements in the list: ").strip().split()))
        myList2 = list(map(str, input("Enter elements for the next list: ").strip().split()))
        dupes = list(set(myList).intersection(myList2))
        print("List A is: ", myList)
        print("List B is: ", myList2)
        print("The intersection is ", dupes)
    if dataType == "integer" :
        myList = list(map(int, input("Enter elements in the list: ").strip().split()))
        myList2 = list(map(int, input("Enter elements for the next list: ").strip().split()))
        dupes = list(set(myList).intersection(myList2))
        print("List A is: ", myList)
        print("List B is: ", myList2)
        print("The intersection is ", dupes)

# The user input is placed in a variable
#dataType = input("Value type for list: ")
# The function finding the similarities between the two lists is called
#intersections(dataType)


# Lab 8c
def main():
    import lab8C
    string = "John Wick"
    lab8C.is_uniques(string)
    string = "Samantha Ahtnamas"
    lab8C.is_uniques(string)
    string = "The quick brown fox jumps over the lazy dog"
    lab8C.is_pangram(string)
    string = "The slow brown wolf jumps over the energetic coyote"
    lab8C.is_pangram(string)


#main()

# Lab 8d
# A dictionary is used and stored in a variable
def main(myWord) :
    sortWord = {}
    # Using a for loop, each value in myWord is passed into sortWord
    for char in myWord :
        if char in sortWord :
            # If a similarity is found the count is incremented
            sortWord[char] += 1
        else :
            # If not then instance of the character at the index is kept
            sortWord[char] = 1
    print("The number of times each letter occurs in the string \"%s\" " 
          % myWord)
    # Print dictionary sortWord key, separate by space
    for key in sortWord :
        print("%s %3s" % (key, sortWord[key]))
    # Function call separator
    print("*" * 100)


main("mathematician")
# Ramanujan inspired function call
main("m" * 100 + "athematicia" + "n" * 100)
