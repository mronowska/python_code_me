txt = input("Wprowadź listę oddzieloną myślnikami: ")
txt_splitted = txt.split('-')
txt_dict = {}
txt_sorted = ""

for word in txt_splitted:
    txt_dict[word.lower()] = word

keys_sorted = sorted(txt_dict.keys())

for key in keys_sorted:
    txt_sorted += txt_dict[key] + "-"

print(txt_sorted[:-1])