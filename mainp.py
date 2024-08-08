#! python3
# Finding elements on the page

import logging, time, webbrowser
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

logging.basicConfig(level = logging.DEBUG, format = '%(asctime)s -  %(levelname)s -   %(message)s')
#logging.disable(logging.CRITICAL)

users = ['pinedah_11', 'faatii._01', 'samueln.ortigoza']

browser = webdriver.Chrome()
browser.get('https://www.instagram.com/' + users[1])

time.sleep(5)

try:

    loginButton = browser.find_element(By.LINK_TEXT, 'Log In')
    loginButton.click()

    time.sleep(5)

    emailForm = browser.find_element(By.TAG_NAME, 'input')
    emailForm.click()
    emailForm.send_keys('papanacho11')
    time.sleep(2)
    emailForm.send_keys(Keys.TAB)
    time.sleep(2)
    emailForm.send_keys('Papanachito')
    time.sleep(3)
    emailForm.send_keys(Keys.ENTER)

    time.sleep(10)
    div_elem = browser.find_elements(By.CLASS_NAME, '_aagv')

    img_elems = []
    srcs = []
    for i in range(len(div_elem)):
        img_elems.append(div_elem[i].find_element(By.TAG_NAME, 'img'))

    for j in range(len(img_elems)):
        srcs.append(img_elems[j].get_attribute('src'))

    for k in range(len(srcs)):
        webbrowser.open(srcs[k])

    
    """img_elem = div_elem.find_element(By.TAG_NAME, 'img')
    print(f"\n\nFound <{img_elem}> element with that class name!\n")
    print(f"\n\nFound <{img_elem.get_attribute('alt')}> element with that class name!\n")
    print(f"\n\nFound <{img_elem.get_attribute('src')}> element with that class name!\n")
    link = img_elem.get_attribute('src')
    webbrowser.open(link)"""
except NoSuchElementException:
    print("Was not able to find an element with that class name.")

# Wait for user input before closing the browser
input("Press Enter to close the browser...")

# Close the browser
browser.quit()