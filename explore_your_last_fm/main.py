import init
import os
import time
import datetime
import page_operations
import handle_file
import Scrobble

songs_tab = []
songs_tab_artist = []
your_index = 100000

#tworzę objekt klasy
song = Scrobble.Scrobble(your_index)

#wchodzę na stronę i akceptuje cookies
page_operations.accept_cookies()

#sprawdzam ile w sumie jest scrobbli
all_scrobbles = song.scrobbles_from_all_time()

#na której stronie jest szukana piosenka
page_index = song.on_which_page_is_your_song(all_scrobbles)
print(f"To czego szukasz jest na stronie: {page_index}")

#przejdź na konkretną str
page_operations.go_to_specific_page(page_index)

songs_tab_ = song.create_tab_of_songs(songs_tab, 'chartlist-name')
time.sleep(1)
songs_tab_artist = song.create_tab_of_songs(songs_tab_artist, 'chartlist-artist')

#init.driver.close()

try:
    os.remove("my_songs_name.csv")
    os.remove("my_songs_artist.csv")
finally:
    f_name = open("my_songs_name.csv", "x")
    f_artist = open("my_songs_artist.csv", "x")

handle_file.write_tab_to_file('my_songs_name.csv', songs_tab)
handle_file.write_tab_to_file('my_songs_artist.csv', songs_tab_artist)

print(f"Liczba wszystkich scrobbli na dzień {datetime.date.today()} to: {all_scrobbles}")
print(f"Indeks, pod którym szukasz piosenki: {your_index}")

how_many_songs_passed_by = (all_scrobbles - your_index) - (page_index-1)*50 - 1

print(f"Jaki indeks w pliku będziemy pobierać: {how_many_songs_passed_by}")

print(f"Tytuł piosenki, której szukasz pod indeksem {your_index} to {init.Color.WARNING}'{handle_file.read_file('my_songs_name.csv', how_many_songs_passed_by)}' {init.Color.FAIL}{handle_file.read_file('my_songs_artist.csv', how_many_songs_passed_by)}{init.Color.ENDC} - niezły numer!")