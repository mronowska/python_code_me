import init
import page_operations
import time
import handle_file
import os

class Scrobble:
    def __init__(self, index):
        self.index = index

    def create_tab_of_songs(self, tab_name, chartlist_atribute):
        try:
            init.WebDriverWait(init.driver, 10).until(
                init.EC.presence_of_element_located((init.By.CLASS_NAME, 'tracklist-section'))
            )

            sections = init.driver.find_elements_by_class_name('tracklist-section')
            for tracklist_section in sections:
                titles = tracklist_section.find_elements_by_class_name(chartlist_atribute)

                for song_title in titles:
                    title = song_title.find_element_by_tag_name('a')
                    tab_name.append(title.text)
                    # print(title.text)

            #zwraca tablicę tytułów dla aktualnie wyświetlanej strony
            return tab_name

        except:
                print("Nie znaleziono klasy tracklist-section")

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