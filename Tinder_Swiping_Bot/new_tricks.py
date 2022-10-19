
# main_page = chrome_webdriver.current_window_handle

# chrome_webdriver.maximize_window()

# window_before = chrome_webdriver.window_handles[0]

# window_after = chrome_webdriver.window_handles[1]

# chrome_webdriver.switch_to.window(window_name=window_after)

# In Selenium, each window has an Identification Handle. New windows that have popped out From the base_window
# are further down in the Array/Sequence. The code to switch to the New pop-up window:
# base_window = chrome_webdriver.current_window_handle
# google_login_window = chrome_webdriver.window_handles[1]
# chrome_webdriver.switch_to.window(window_name=google_login_window)
# print(chrome_webdriver.title)
# Now revert to the base_window and print the title of the Selenium controlled window.
# chrome_webdriver.switch_to.window(window_name=base_window)
# print(chrome_webdriver.title)


# Alternative Ending

# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.chrome.options import Options

# chrome_options = Options()
# chrome_options.add_experimental_option("detach", True)
# s=Service(ChromeDriverManager().install())
# chrome_webdriver = webdriver.Chrome(service=s, options=chrome_options)

# for n in range(10):
#     try:
#         sleep(1)
#         ActionChains(chrome_webdriver).send_keys(Keys.ARROW_RIGHT).perform()
#     except NoSuchElementException:
#         sleep(3)
#         print("not found")
#         ActionChains(chrome_webdriver).send_keys(Keys.ESCAPE).perform()
#     else:
#         print("like!")
#         sleep(1)
#         ActionChains(chrome_webdriver).send_keys(Keys.ESCAPE).perform()
#         ActionChains(chrome_webdriver).send_keys(Keys.ESCAPE).perform()


# Alternative Ending

# for i in range(100):
#     sleep(1)
#     try:
#         like_button.click()
#     except NoSuchElementException:
#         print("Like button not available")
#         sleep(3)
#         continue
#     except ElementClickInterceptedException:
#         back_to_tinder = chrome_webdriver.find_element(By.XPATH, "//*[@id='q573898311']/main/div/div[1]/div/div[4]")
#         back_to_tinder.click()
#         sleep(3)
#         continue
