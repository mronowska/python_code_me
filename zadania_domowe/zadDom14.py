words = input("Podaj zdanie: ")

count_uppercase = 0
count_lowercase = 0

for word in words:
    if word.isupper() == True:
        count_uppercase += 1
    if word.islower() == True:
        count_lowercase += 1

print(f"W zdaniu jest {count_uppercase} wielkich liter i {count_lowercase} małych.")