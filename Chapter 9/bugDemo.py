from LA_bug import Bug


def main():
    bugsy = Bug(10)
    bugsy.move()  # Now the position is 11
    print("Expected %d: Actual: %d"
          % (bugsy.getPosition(), bugsy.getPosition()))
    bugsy.turn()
    bugsy.move()  # Now the position is 10
    print("Expected %d: Actual: %d"
          % (bugsy.getPosition(), bugsy.getPosition()))
    bugsy.turn()
    for i in range(100):
        bugsy.move()  # Now the position is 110
    print("Expected %d: Actual: %d"
          % (bugsy.getPosition(), bugsy.getPosition()))


main()
