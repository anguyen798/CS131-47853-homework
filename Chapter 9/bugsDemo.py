def main(): 
    from IC_Bug import Bug
    bugsy = Bug(10.0)
    bugsy.move()
    print("Expected %d: Actual: %d"
          % (bugsy.getPosition(), bugsy.getPosition()))    
    bugsy.turn()
    bugsy.move()
    print("Expected %d: Actual: %d"
          % (bugsy.getPosition(), bugsy.getPosition()))
main()
