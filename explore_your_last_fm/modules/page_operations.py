import init

def accept_cookies():
    searh_btn_accept_cookies = init.driver.find_element_by_id('onetrust-accept-btn-handler')
    searh_btn_accept_cookies.click()

def display_songs_list():
    search_more_link = init.driver.find_element_by_link_text('Więcej utworów')
    search_more_link.click()

def next_page_of_songs_list():
    search_more_link = init.driver.find_element_by_link_text('Następna')
    search_more_link.click()
