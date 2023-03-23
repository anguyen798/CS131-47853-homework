with open("Lab7bOutput.txt", "w") as outputFile :
    lineHeading = 1
    with open("Lab7bInput.txt", "r") as inputFile :
        for line in inputFile :
            lineText = line.strip()
            outputFile.write("/* %d */ %s\n" % (lineHeading, lineText))
            lineHeading = lineHeading + 1
