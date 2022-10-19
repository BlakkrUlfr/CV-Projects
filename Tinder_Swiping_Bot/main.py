from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException

from time import sleep

FB_EMAIL = ''
FB_PASSWORD = ''

chrome_driver_path = Service(executable_path="C:/Users/Admin/OneDrive/Υπολογιστής/chromedriver.exe")
chrome_webdriver = webdriver.Chrome(service=chrome_driver_path)

chrome_webdriver.get(url='https://tinder.com/')

base_window = chrome_webdriver.current_window_handle
# main_window = chrome_webdriver.window_handles[0]
chrome_webdriver.maximize_window()

sleep(3)

decline_cookies_button = chrome_webdriver.find_element(by=By.XPATH,
                                                       value='//*[@id="t1452431810"]/div/div[2]/'
                                                             'div/div/div[1]/div[2]/button')
decline_cookies_button.click()

sleep(3)

login_button = chrome_webdriver.find_element(by=By.XPATH,
                                             value='//*[@id="t1452431810"]/div/div[1]/div/main/div[1]/'
                                                   'div/div/div/div/header/div/div[2]/div[2]')
login_button.click()

sleep(3)

fb_login_button = chrome_webdriver.find_element(by=By.XPATH,
                                                value='//*[@id="t-275949266"]/main/div/div[1]/div/div/div[3]/'
                                                      'span/div[2]/button')
fb_login_button.click()

sleep(5)

fb_login_window = chrome_webdriver.window_handles[1]

chrome_webdriver.switch_to.window(window_name=fb_login_window)
print(chrome_webdriver.title)

fb_cookies_button = chrome_webdriver.find_element(by=By.XPATH, value='//*[@id="u_0_a_3H"]')
fb_cookies_button.click()

sleep(1)

email_input = chrome_webdriver.find_element(by=By.XPATH, value='//*[@id="email"]')
email_input.send_keys(FB_EMAIL)

password_button = chrome_webdriver.find_element(by=By.XPATH, value='//*[@id="pass"]')
password_button.send_keys(FB_PASSWORD)

final_login_button = chrome_webdriver.find_element(by=By.XPATH, value='//*[@id="buttons"]')
final_login_button.click()

chrome_webdriver.switch_to.window(window_name=base_window)
print(chrome_webdriver.title)

sleep(3)

allow_location_button = chrome_webdriver.find_element(by=By.XPATH, value='//*[@id="modal-manager"]/div/div/div/div/'
                                                                         'div[3]/button[1]')
allow_location_button.click()

notifications_button = chrome_webdriver.find_element(by=By.XPATH, value='//*[@id="modal-manager"]/div/div/div/div/'
                                                                        'div[3]/button[2]')
notifications_button.click()

cookies = chrome_webdriver.find_element(by=By.XPATH, value='//*[@id="content"]/div/div[2]/div/div/div[1]/button')
cookies.click()

# Tinder's free tier only allows 100 "Likes" per day.
# If you have a premium account, feel free to change to a while loop.
for n in range(stop=100):

    like_button = chrome_webdriver.find_element(by=By.XPATH, value='//*[@id="t1452431810"]/div/div[1]/div/div/main/'
                                                                   'div/div/div[1]/div/div[5]/div/div[4]/button')

    matched_popup = chrome_webdriver.find_element(by=By.XPATH, value='//*[@id="q573898311"]/main/div/div[1]/'
                                                                     'div/div[4]')
    # Add a 1-second delay between Likes.
    sleep(1)

    try:
        print("called")
        like_button.click()
    # Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
    except ElementClickInterceptedException:
        try:
            matched_popup.click()
        except NoSuchElementException:
            sleep(5)
            matched_popup.click()
    # Catches the cases where the "Like" button has not yet loaded, so wait 3 seconds before retrying.
    except NoSuchElementException:
        sleep(5)
        like_button.click()

chrome_webdriver.quit()


