from IC1_SodaCan import SodaCan


def main():
    canNumber = 1

    while True:
        try:
            height = input("Enter the height of the can (type a word, zero, or"
                           " negative value to stop): ")
            height = float(height)
            if height <= 0:
                break
        except ValueError:
            break

        try:
            radius = input("Enter the radius of the can (type a word, zero or"
                           " negative value to stop): ")
            radius = float(radius)
            if radius <= 0:
                break
        except ValueError:
            break

        can = SodaCan(height, radius, canNumber)

        can.getSurfaceArea()
        can.getVolume()
        print("*" * 100)

        canNumber = canNumber + 1


main()
