from PA_Car import Car

def main() :
 
    myHybrid = Car(50) # 50 miles per gallon
    myHybrid.addGas(20) # Tank 20 gallons
    myHybrid.drive(100) # Drive 100 miles
    print(myHybrid.getGasLevel()) # Print fuel remaining


main()
