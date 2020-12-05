from selenium import webdriver
#do klikania enter itp
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import csv
import time
count_songs = 0


PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)
driver.get('https://www.last.fm/pl/user/Dess066')

#driver.close() zamknięcie danej karty
#drive.quit() zamknięcie całej przeglądarki
#driver.title tytuł strony