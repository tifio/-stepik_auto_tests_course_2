import time
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_button_search(browser):
    browser.get(link)
    item = browser.find_elements(By.CLASS_NAME, "btn-add-to-basket")
    assert item, 'no item!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
    time.sleep(5)