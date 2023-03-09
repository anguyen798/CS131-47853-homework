# Lab 5a
def find_sum(n) :
    print("Enter an integer: %d" % n)  # emulate input()
    sum_n = 0
    for i in range(1, n + 1) :
        sum_n = sum_n + i
    print("The result is %d" % sum_n)


find_sum(10)
find_sum(3)


# Lab 5b
def volume_rectangle(length, width, height) :
    print("Enter the length: %d" % length)  # emulate input()
    print("Enter the width: %d" % width)
    print("Enter the height: %d" % height)
    volume = length * width * height
    print("A rectangular prism with dimensions %d, %d, %d has a volume of %d"
          % (length, width, height, volume))

volume_rectangle(3,4,2)