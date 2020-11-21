#tak staramy się nie robić

file = open("text.txt", encoding="utf-8")
file.close() #pamietac o zamknieciu


#lepiej tak
with open(text.txt, encoding="utf-8") as file:
    print(file)