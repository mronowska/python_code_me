#nie uwzgledniam, jesli niektore wyrazy beda z wielkiej litery, inne z malej. Jesli to konieczne, to wrzuc uwage

words = input("Podaj wyrazy rozdzielone myślnikiem: ")

sorted_list = sorted(words.split('-'))
print(sorted_list)

separator = '-'

separator = separator.join(sorted_list)
print(separator)

