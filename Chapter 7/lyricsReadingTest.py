with open(lyrics.txt, 'r') as lyrics:
    for line in lyrics:
        line = line.rstrip()
        wordList = line.split()
        for word in wordList :
            word = word.rstrip(".,?!")
            print(word)
    inputFile.close()