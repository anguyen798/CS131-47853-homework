# Lab 3a
purchasePrice = int(input("Please enter the total purchase price: "))
if purchasePrice < 128:
    purchasePriceDiscount = purchasePrice * 0.08
    purchasePriceAfterDiscount = purchasePrice - purchasePriceDiscount
    print("The price after the discount is $ %s" % purchasePriceAfterDiscount)
elif purchasePrice >= 128:
    purchasePriceDiscount = purchasePrice * 0.16
    purchasePriceAfterDiscount = purchasePrice - purchasePriceDiscount
    print("The price after the discount is $ %s" % purchasePriceAfterDiscount)

# Lab 3b
shippingInternational = input("Are you shipping internationally (yes or no)? ")
print(shippingInternational)
if shippingInternational in ["yes", "Yes", "y", "Y"]:  # using in same as: or var = "yes" or var =="Yes", ...
    shippingContinental = input("Are you shipping continental (yes or no)?")
    if shippingContinental in ["yes", "Yes", "y", "Y"]:
        shippingRate = 5
    elif shippingContinental in ["no", "No", "n", "N"]:
        shippingRate = 10
    print("The shipping rate is $%.2f" % shippingRate)
else:
    shippingRate = 10
    print("The shipping rate is $%.2f" % shippingRate)


# Lab 3c

def lab3c_sort(int1, int2, int3):  # Creating function to input test cases as function parameters
    sorted_list = [int1, int2, int3]
    sorted_list = sorted(sorted_list)
    print("%s %s %s becomes %s %s %s" % (int1, int2, int3, sorted_list[0], sorted_list[1], sorted_list[2]))

lab3c_sort(4, 7, 3)  # test case 1 using default integers
lab3c_sort(9, 1, 1)  # test case 2 using random integers


# Lab 3d
firstInteger = int(input("Enter the first integer: "))
secondInteger = int(input("Enter the second integer: "))
thirdInteger = int(input("Enter the third integer: "))

if firstInteger == secondInteger == thirdInteger:
    print("They are all the same.")
elif firstInteger != secondInteger != thirdInteger != firstInteger:
    print("They are all different.")
elif firstInteger != secondInteger and firstInteger != thirdInteger and secondInteger != thirdInteger:
    print("They are all different.")
else:
    print("They are neither all the same nor all different.")


# Lab 3e
str = " Hello, World"
print("The number of l's is %s" % str.count("l"))
print('***' + str.strip() + '***')
print('***' + str.lstrip() + '***')
print('***' + str.rstrip() + '***')
print(str.replace('l', '*').replace('o', '*'))
