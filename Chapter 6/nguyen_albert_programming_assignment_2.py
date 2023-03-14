# Programming Assignment 2 - 6A
def exercise_a_part_one() :  # using functions to keep list variable local and call
    list = [1, 2, 3, 4, 5, 6]
    # Reverse the list using slice
    listReverse = list[::-1]  # start at [0], negative step
    print(listReverse)
    print("*" * 30)


def exercise_a_part_two() :
    list = [4, 6, 8, 6, 12]
    # Create a new list without 6
    listWithoutSix = []
    for digit in list :
        if digit != 6 :
            listWithoutSix.append(digit)
    print(listWithoutSix)
    print("*" * 30)

    
def exercise_a_part_three() :
    counter = 0
    list = [5, 10, 15, 200, 25, 50, 20]
    # Create a list where only the first instance of 20 is replaced with 200
    listReplaced = []
    for digit in list :
        if digit == 20 and counter == 0:
            digit = 200
            counter = counter + 1
        listReplaced.append(digit)
    print(listReplaced)
    print("*" * 30)


def exercise_a_part_four() :
    list1 = ["M", "na", "i", "Ke"]
    list2 = ["y", "me", "s", "lly"]
    listCombined = []
    # Append together using range of [0, 4]because exactly 4 list elements each
    for i in range(0, len(list1)):
        listCombined.append(list1[i] + list2[i])
    print(listCombined)
    print("*" * 30)

        
# Programming Assignment 2 - 6B
def exercise_b() :
    sum = 0
    list = [1, 4, 9, 16, 9, 7, 4, 9, 11]
    alternatingList = []
    for i in range(0, len(list)):
        if i // 2 == 0 :
            number = list[i] * -1
        elif i//2 != 0 :
            number = list[i]
        alternatingList.append(number)
    print(alternatingList)
    print("*" * 30)



exercise_a_part_one()       
exercise_a_part_two()
exercise_a_part_three()
exercise_a_part_four()
exercise_b()


