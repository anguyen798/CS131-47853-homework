list = [32.0, 54.0, 67.5, 80.25, 115.0]
listTotal = sum(list)
listAverage = listTotal / len(list)

with open('3aOutput.txt', 'w') as outputFile:
    for integer in list :
        outputFile.write('%.2f\n' % integer)
    outputFile.write('-' * 20 + '\n')
    outputFile.write('Total: %.2f\n' % listTotal)
    outputFile.write('Total: %.2f\n' % listAverage)
