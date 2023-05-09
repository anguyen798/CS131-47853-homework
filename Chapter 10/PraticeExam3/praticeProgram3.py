# Q1
stringVariable = input("Enter a string here: ")
stringList = list(stringVariable)
print(stringList)
stringDict = dict()
for letter in stringList :
    stringDict.update({letter: len(letter)})

print(stringDict)


def main() :
    letterDictionary("extraordinary")
    
    def letterDictionary(word) :
        dictionaryW = {}
        for letter in word :
            if letter in dictionaryW :
                dictionaryW[letter] = dictionaryW[letter] + 1
            else :
                dictionaryW[letter] = 1


#print("%-2s %3d" % (string

# Q2
# See IC_student.py and studentDemo.py

# Q3
# See persons.py and personDemo.py