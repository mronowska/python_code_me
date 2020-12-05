import init
import page_operations
import class_Scrobble



# page_operations.accept_cookies()
# song.scrobbles_from_all_time()
# song.review_songs_list()
# count_songs = count_songs + len(count_songs_on_sections())
# print(f"Liczba piosenek w wyświetlonych sekcjach: {count_songs}")
# page_operations.next_page()
# init.time.sleep(1)
# count_songs_on_sections()
# #count_songs = count_songs + len(count_songs_on_sections())
# print(f"Liczba piosenek w wyświetlonych sekcjach: {count_songs}")























# from selenium import webdriver
# #do klikania enter itp
# from selenium.webdriver.common.keys import Keys
#
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# import csv
# import time
# count_songs = 0
#
#
# PATH = "C:\Program Files (x86)\chromedriver.exe"
#
# driver = webdriver.Chrome(PATH)
# driver.get('https://www.last.fm/pl/user/Dess066')
#
# #driver.close() zamknięcie danej karty
# #drive.quit() zamknięcie całej przeglądarki
# #driver.title tytuł strony

# def scrobbles_from_all_time():
#     searh_scrobbles_from_all_time = driver.find_element_by_class_name('header-metadata-display')
#     scrobbles_as_string = searh_scrobbles_from_all_time.text
#     scrobbles_as_num = int(scrobbles_as_string.replace(" ", ""))
#
#     return scrobbles_as_num

# def display_song_from_chosen_index(all_scrobbles, index):
#     x = all_scrobbles - index
#     return x

# def accept_cookies():
#     searh_btn_accept_cookies = driver.find_element_by_id('onetrust-accept-btn-handler')
#     searh_btn_accept_cookies.click()
#
# def review_songs_list():
#     search_more_link = driver.find_element_by_link_text('Więcej utworów')
#     search_more_link.click()
#
# def next_page():
#     search_more_link = driver.find_element_by_link_text('Następna')
#     search_more_link.click()

# def write_tab_to_file(filename,  tab_length, tab = []):
#     with open(filename, mode="w", encoding="utf-8") as file:
#         content = []
#         for i in tab:
#             content.append(str(i))
#             content.append(', ')
#         file.writelines(content)

# def create_tab_of_songs():
#     titles_tab = []
#     try:
#         WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.CLASS_NAME, 'tracklist-section'))
#         )
#
#         sections = driver.find_elements_by_class_name('tracklist-section')
#         for tracklist_section in sections:
#             titles = tracklist_section.find_elements_by_class_name('chartlist-name')
#
#             for song_title in titles:
#                 title = song_title.find_element_by_tag_name('a')
#                 titles_tab.append(title.text)
#                 #print(title.text)
#
#         return titles_tab
#
#     finally:
#         pass
#         #driver.quit()




#write_tab_to_file('plik_testowy.csv', len(count_songs_on_sections()), count_songs_on_sections())


# try:
#     WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.CLASS_NAME, 'tracklist-section'))
#     )
#
#     sections = driver.find_elements_by_class_name('tracklist-section')
#     for tracklist_section in sections:
#
#         titles = tracklist_section.find_elements_by_class_name('chartlist-name')
#
#         for artist in titles:
#             title = artist.find_element_by_tag_name('a')
#             print(title.text)
#
#
# finally:
#     search_main = driver.find_element_by_class_name('col-main')
#     driver.close()

