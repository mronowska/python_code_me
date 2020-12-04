def extractListOfLines(fileName):
    f = open(fileName, "r", encoding="utf-8")
    listofLines = f.read().split("\n")
    f.close()
    return listofLines


def compareLines(lines1, lines2):
    lines1Len = len(lines1)
    lines2Len = len(lines2)
    if lines1Len > lines2Len:
        shorterLength = lines2Len
        biggerLength = lines1Len
        isLines1Longer = True
    else:
        shorterLength = lines1Len
        biggerLength = lines2Len
        isLines1Longer = False
    return [isLines1Longer, shorterLength, biggerLength]


lines1 = extractListOfLines("sciernisco.txt")
lines2 = extractListOfLines("na_zdrowie.txt")

data = compareLines(lines1, lines2)
shorterLength = data[1]
biggerLength = data[2]

for i in range(shorterLength):
    print(f"{lines1[i]}\n{lines2[i]}")

for i in range(shorterLength, biggerLength):
    if data[0]:
        print(lines1[i])
    else:
        print(lines2[i])