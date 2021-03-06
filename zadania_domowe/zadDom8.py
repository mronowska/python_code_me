text = '''Thunder, thunder, thunder, thunder
I was caught
In the middle of a railroad track
I looked round
And I knew there was no turning back
My mind raced
And I thought what could I do
And I knew
There was no help, no help from you
Sound of the drums
Beating in my heart
The thunder of guns
Tore me apart
You've been
Thunderstruck
Rode down the highway
Broke the limit, we hit the town
Went through to Texas, yeah Texas, and we had some fun
We met some girls
Some dancers who gave a good time
Broke all the rules
Played all the fools
Yeah yeah they, they, they blew our minds
And I was shaking at the knees
Could I come again please
Yeah them ladies were too kind
You've been
Thunderstruck
I was shaking at the knees
Could I come again please
Thunderstruck, Thunderstruck, Thunderstruck, Thunderstruck
It's alright, we're doin' fine
It's alright, we're doin' fine, fine, fine
Thunderstruck, yeah, yeah, yeah
Thunderstruck, Thunderstruck
Thunderstruck, baby, baby
Thunderstruck, you've been Thunderstruck
Thunderstruck, Thunderstruck
You've been Thunderstruck'''

text = text.split()
slownik = {}

for i in text:
    try:
        slownik[i]
    except KeyError:
        slownik[i] = 0
    finally:
        slownik[i] += 1

[print('Wyraz "{}" wystopuje w tekście "{}" razy'.format(word, count)) for word, count in slownik.items()]


## inne rozwiązanie - z zajęć
text2 = "Sto lat, sto lat, niech żyje, żyje nam"
liczba_wystapien_slow = {}
text = text2.replace(",", "")
lista_slow = text2.split()
for slowo in lista_slow:
    liczba_wystapien = liczba_wystapien_slow.get(slowo, 0)
    liczba_wystapien_slow[slowo] = liczba_wystapien + 1

print(liczba_wystapien_slow)
