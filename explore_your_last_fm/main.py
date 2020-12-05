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
searh_btn_accept_cookies = driver.find_element_by_id('onetrust-accept-btn-handler')
search_more_link = driver.find_element_by_link_text('Więcej utworów')
searh_btn_accept_cookies.click()
search_more_link.click()

try:
    chartlist_row = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'chartlist-row'))
    )

    artists = chartlist_row.find_elements_by_class_name('chartlist-name')

    for artist in artists:
        title = artist.find_element_by_tag_name('a')
        print(title.text)

finally:
    print("Zamykam")


#count_row = driver.find_elements_by_class_name('chartlist-row')
#print(count_row)
