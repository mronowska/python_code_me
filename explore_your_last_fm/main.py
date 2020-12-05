import init
import os
import time
import datetime
import page_operations
import handle_file
import Scrobble

songs_tab = []
your_index = 101253

#tworzę objekt klasy
song = Scrobble.Scrobble(your_index)

#wchodzę na stronę i akceptuje cookies
page_operations.accept_cookies()

#sprawdzam ile w sumie jest scrobbli
all_scrobbles = song.scrobbles_from_all_time()

#na której stronie jest szukana piosenka
page_index = song.on_which_page_is_your_song(all_scrobbles)
print(f"To czego szukasz jest na stronie: {page_index}")

#przejdź na stronę ze spisem piosenek
page_operations.display_songs_list()
time.sleep(1)
songs_tab = song.create_tab_of_songs(songs_tab)

if page_index > 1:
    for i in range(page_index - 1):
        print(f"iteracja: {i}")
        time.sleep(1)
        songs_tab = song.create_tab_of_songs(songs_tab)
        time.sleep(1)
        print(len(songs_tab))
        time.sleep(1)
        page_operations.next_page_of_songs_list()
        time.sleep(1)

time.sleep(1)

try:
    os.remove("my_songs.csv")
finally:
    f = open("my_songs.csv", "x")

handle_file.write_tab_to_file('my_songs.csv', songs_tab)

print(f"Liczba wszystkich scrobbli na dzień {datetime.date.today()} to: {all_scrobbles}")
print(f"Indeks, pod którym szukasz piosenki: {your_index}")
how_many_songs_passed_by = all_scrobbles - your_index
print(f"Jaki indeks w pliku będziemy pobierać: {how_many_songs_passed_by}")
handle_file.read_file('my_songs.csv', how_many_songs_passed_by)