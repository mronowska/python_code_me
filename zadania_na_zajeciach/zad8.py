lista_for = []
lista_while = []

#for
for i in range (0, 101):
    if i % 3 == 0 and i % 2 == 0:
        print(i)
        lista_for.append(i)

#while

i = 0
while i <= 100:
    if i % 2 == 0 and i % 3 == 0:
        print(i)
        lista_while.append(i)
    i += 1

print(lista_for == lista_while)