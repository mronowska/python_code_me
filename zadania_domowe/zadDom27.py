import os, collections

def writeToFile():
    try:
        os.remove("plik.txt")
    finally:
        f = open("plik.txt", "x")

    for i in range(4):
        line = input("Linijka " + str(i) + ": ")
        if i < 3: f.write(line + "\n")
        else: f.write(line)
    f.close()

def readFile():
    f = open("plik.txt", "r")
    content = f.read()
    words = content.split("\n")
    f.close()
    return words

def printAllLines(words):
    for i in range(len(words)):
        print(f"Linijka {str(i)}: '{words[i]}', długość tego wiersza to {len(words[i])}")

def printMostCommonLetter():
    f = open("plik.txt", "r")
    content = f.read()
    c = collections.Counter(content)
    print(f"Najpopularniejszy znak to: {c.most_common(1)[0][0]}")
    f.close()

def printMostCommonWord(words):
    text = ""
    for word in words:
            text += word
    words2 = text.split(" ")

    c = collections.Counter(words)
    print(f"Najpopularniejszy wyraz to: {c.most_common(1)[0][0]}")

writeToFile()
printAllLines(readFile())
printMostCommonLetter()
printMostCommonWord(readFile())
