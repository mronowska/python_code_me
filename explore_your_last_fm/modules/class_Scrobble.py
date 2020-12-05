import init
import page_operations
import time
import handle_file
import os

songs_tab = []

class Scrobble:
    def __init__(self, index):
        self.index = index


    def create_tab_of_songs(self, tab_name):

        try:
            init.WebDriverWait(init.driver, 10).until(
                init.EC.presence_of_element_located((init.By.CLASS_NAME, 'tracklist-section'))
            )

            sections = init.driver.find_elements_by_class_name('tracklist-section')
            for tracklist_section in sections:
                titles = tracklist_section.find_elements_by_class_name('chartlist-name')

                for song_title in titles:
                    title = song_title.find_element_by_tag_name('a')
                    tab_name.append(title.text)
                    # print(title.text)

            #zwraca tablicę tytułów dla aktualnie wyświetlanej strony
            return tab_name

        finally:
                pass
                #init.driver.quit()

    def scrobbles_from_all_time(self):
        searh_scrobbles_from_all_time = init.driver.find_element_by_class_name('header-metadata-display')
        scrobbles_as_string = searh_scrobbles_from_all_time.text
        scrobbles_as_num = int(scrobbles_as_string.replace(" ", ""))
        return scrobbles_as_num

    def on_which_page_is_your_song(self, all_scrobbles):
        x = int(all_scrobbles) - int(self.index)
        which_page = x / 50
        if x % 50 != 0:
            which_page += 1

        return int(which_page)

    def which_song_in_turn(self):
        pass


your_index = 101253

#tworzę objekt klasy
song = Scrobble(your_index)

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

print(f"Wszystkie scrobble: {all_scrobbles}")
print(f"Twój indeks: {your_index}")
how_many_songs_passed_by = all_scrobbles - your_index
print(f"Ile leci do pliku: {how_many_songs_passed_by}")
handle_file.read_file('moje_piosenki7.csv', how_many_songs_passed_by)




#
# page_operations.accept_cookies()
#
# all_scrobbles = song.scrobbles_from_all_time()
# print(f"Masz aż {all_scrobbles} scrobbli!")
#
# page_operations.display_songs_list()
#
# init.count_songs = init.count_songs + len(song.create_tab_of_songs())
# print(f"Liczba piosenek w wyświetlonych sekcjach: {init.count_songs}")
#
# time.sleep(1)
# page_operations.next_page_of_songs_list()
# time.sleep(1)
# songs_tab = song.create_tab_of_songs()
# handle_file.write_tab_to_file('spis_piosenek.csv', len(songs_tab), songs_tab)

#count_songs = count_songs + len(count_songs_on_sections())
# print(f"Liczba piosenek w wyświetlonych sekcjach: {init.count_songs}")
# time.sleep(1)
# print(f"Strona Twojej piosenki: {song.on_which_page_is_your_song(all_scrobbles)}")






