from selenium import webdriver
#do klikania enter itp
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)
driver.get('https://www.last.fm/pl/user/Dess066')

#driver.close() zamknięcie danej karty
#drive.quit() zamknięcie całej przeglądarki
#driver.title tytuł strony

def accept_cookies():
    searh_btn_accept_cookies = driver.find_element_by_id('onetrust-accept-btn-handler')
    searh_btn_accept_cookies.click()

def review_songs_list():
    search_more_link = driver.find_element_by_link_text('Więcej utworów')
    search_more_link.click()

def count_songs_on_sections():
    titles_tab = []
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'tracklist-section'))
        )

        sections = driver.find_elements_by_class_name('tracklist-section')
        for tracklist_section in sections:
            titles = tracklist_section.find_elements_by_class_name('chartlist-name')


            for artist in titles:
                title = artist.find_element_by_tag_name('a')
                titles_tab.append(title.text)
                print(title.text)

            print(len(titles_tab))

        return len(titles_tab)


    finally:
        driver.close()


accept_cookies()
review_songs_list()
print(count_songs_on_sections())


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

