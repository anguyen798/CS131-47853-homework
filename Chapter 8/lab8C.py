def is_uniques(string):
    originalString = string
    string = string.lower()
    string = string.replace(" ", "")
    if len(string) == len(set(string)) :
        unique = True
    else :
        unique = False
    print("The string \"%s\" has unique characters? %s"
          % (originalString, unique))
    return unique


def is_pangram(string) :
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    string = string.lower()
    stringSet = set(string)
    for letter in alphabet :
        if letter not in stringSet :
            print("The string %s is not a pangram!" % string)
            return
    print("The string %s is a pangram!" % string)