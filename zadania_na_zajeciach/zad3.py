song = input("Podaj tytuł ulubionej piosenki: ")

print(f"\n1. Ma ona {len(song)} znaków")
print(f"2. Litera 'a' wystąpiła {song.count('a')} razy")
print(f"3. Hm. Czy w tytule występuje spacja? {' ' in song}")
print(f"4. Wstawianie gwiazdki co znak: {'*'.join(song)}")
print(f"5. Usuwanie spacji: {song.replace(' ', '')}")
