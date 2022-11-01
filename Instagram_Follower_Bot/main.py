from selenium import webdriver

from selenium.common import TimeoutException, ElementClickInterceptedException
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By

from time import sleep

CHROME_DRIVER_PATH = "C:/Users/Admin/OneDrive/Υπολογιστής/chromedriver.exe"
SIMILAR_ACCOUNT = 'chefsteps'
USERNAME = 'Qwerdfasb'
PASSWORD = 'gr-67WHj7SZDCvi'


class InstagramFollower:

    def __init__(self):

        options = Options()
        options.headless = True
        service = Service(executable_path=CHROME_DRIVER_PATH)
        self.chromedriver = webdriver.Chrome(service=service, options=options)

    def login(self):

        self.chromedriver.get(url='https://www.instagram.com/')
        self.chromedriver.maximize_window()

        try:
            WebDriverWait(driver=self.chromedriver, timeout=15).until(
                method=EC.presence_of_element_located((By.CLASS_NAME, '_a9--')))
        except TimeoutException:
            self.chromedriver.quit()
        else:
            cookies = self.chromedriver.find_element(by=By.CLASS_NAME, value='_a9--')
            cookies.click()

        sleep(1)
        login_username = self.chromedriver.find_element(by=By.NAME, value='username')
        login_username.send_keys(USERNAME)

        sleep(1)
        login_password = self.chromedriver.find_element(by=By.NAME, value='password')
        login_password.send_keys(PASSWORD)

        login_button = self.chromedriver.find_element(by=By.XPATH, value='//*[@id="loginForm"]/div/div[3]/button/div')
        login_button.click()

        try:
            WebDriverWait(driver=self.chromedriver, timeout=15).until(
                method=EC.presence_of_element_located((By.CLASS_NAME, '_ac8f')))
        except TimeoutException:
            self.chromedriver.quit()
        else:
            information = self.chromedriver.find_element(by=By.CLASS_NAME, value='_ac8f')
            information.click()

        try:
            WebDriverWait(driver=self.chromedriver, timeout=15).until(
                method=EC.presence_of_element_located((By.CLASS_NAME, '_a9_1')))
        except TimeoutException:
            self.chromedriver.quit()
        else:
            notifications = self.chromedriver.find_element(by=By.CLASS_NAME, value='_a9_1')
            notifications.click()

    def find_followers(self):

        self.chromedriver.get(url=f'https://www.instagram.com/{SIMILAR_ACCOUNT}')
        self.chromedriver.maximize_window()

        try:
            WebDriverWait(driver=self.chromedriver, timeout=15).until(
                method=EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/chefsteps/followers/']")))
        except TimeoutException:
            self.chromedriver.quit()
        else:
            followers = self.chromedriver.find_element(by=By.CSS_SELECTOR, value="a[href='/chefsteps/followers/']")
            followers.click()

        # Scroll Down in a Pop-Up Window!
        try:
            WebDriverWait(driver=self.chromedriver, timeout=15).until(
                method=EC.presence_of_element_located((By.CLASS_NAME, '_aano')))
        except TimeoutException:
            self.chromedriver.quit()
        else:
            modal = self.chromedriver.find_element(by=By.CLASS_NAME, value='_aano')
            for _ in range(5):
                sleep(3)
                self.chromedriver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', modal)

    def follow(self):

        potential_followers = self.chromedriver.find_elements(by=By.CLASS_NAME, value='_acan')
        for potential_follower in potential_followers:
            if potential_follower.text == "Follow":

                webdriver.ActionChains(driver=self.chromedriver).move_to_element(to_element=potential_follower).click(
                    on_element=potential_follower).perform()

                sleep(1)
            elif potential_follower.text == 'Following' or potential_follower.text == 'Requested':
                continue

        # for potential_follower in potential_followers:
        #     try:
        #         potential_follower.click()
        #         sleep(1)
        #     except ElementClickInterceptedException:
        #         cancel_button = self.chromedriver.find_element(by=By.XPATH, value='//*[@id="mount_0_0_2I"]/div/div/'
        #                                                                           'div/div[2]/div/div/div[2]/div/div/'
        #                                                                           'div[1]/div/div[2]/div/div/div/div/'
        #                                                                           'div[2]/div/div/div[3]/button[2]')
        #         cancel_button.click()


bot = InstagramFollower()

bot.login()

bot.find_followers()

bot.follow()