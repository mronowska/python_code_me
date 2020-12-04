import os, collections
from collections import Counter

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
    print(f"Najpopularniejszy znak to: {c.most_common(1)}")
    f.close()

def printMostCommonWord(words):
    text2 = ""
    for word in words:
            text2 += word
    myDict = Counter(text2.split())
    myList = [k for k, v in myDict.items() if v > 1]
    print(myList)

writeToFile()
printAllLines(readFile())
printMostCommonLetter()
printMostCommonWord(readFile())
