text = input("Podaj wyraz/zdanie: ")
reverse_text = text[::-1]

if text == reverse_text:
    print("O tak, to na pewno palindrom.")
else:
    print("Przykro mi, nie tym razem...")

