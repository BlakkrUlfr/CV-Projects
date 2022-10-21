from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException

from time import sleep
import datetime

ISP_DOWNLOAD_SPEED = 50
ISP_UPLOAD_SPEED = 10

CHROME_DRIVER_PATH = "C:/Users/Admin/OneDrive/Υπολογιστής/chromedriver.exe"

SPEED_TEST_URL = 'https://www.speedtest.net/'

TWITTER_URL = 'https://twitter.com/'
TWITTER_EMAIL = 'ogamwtomounithspanagias@gmail.com'
TWITTER_PASSWORD = 'opkodikos123'

options = Options().add_argument(argument='start-maximized')


class InternetSpeedTwitterBot:

    def __init__(self):
        self.webdriver = webdriver.Chrome(service=Service(executable_path=CHROME_DRIVER_PATH), options=options)
        self.upload = None
        self.download = None

    def get_internet_speed(self):
        self.webdriver.get(url=SPEED_TEST_URL)
        go_button = self.webdriver.find_element(by=By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/'
                                                                   'div[2]/div[3]/div[1]/a')
        try:
            go_button.click()

        except ElementClickInterceptedException:
            self.webdriver.find_element(by=By.XPATH, value='//*[@id="onetrust-accept-btn-handler"]').click()

            sleep(3)
            go_button.click()

        test_complete_str = ""
        # This is the First Sentence of the HIDDEN TEXT that indicated when the test is over.
        test_complete_message = "Your speed test has completed."

        while test_complete_message not in test_complete_str:

            try:
                # Checks for Hidden Text indicating if the test is still running.
                test_complete_str = self.webdriver.find_element(by=By.XPATH, value="/html/body/div[1]").text
                print(test_complete_str)
                sleep(1)
            except:
                sleep(1)

        self.download = self.webdriver.find_element(by=By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/'
                                                                       'div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/'
                                                                       'div[1]/div[2]/div/div[2]/span').text
        self.upload = self.webdriver.find_element(by=By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/'
                                                                     'div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/'
                                                                     'div[1]/div[2]/div/div[2]/span').text

    def tweet_at_isp(self):
        self.webdriver.get(url=TWITTER_URL)

        self.webdriver.implicitly_wait(15)

        cookies = self.webdriver.find_element(by=By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div[2]/'
                                                                 'div[2]/div')
        cookies.click()

        sleep(3)

        signin_button = self.webdriver.find_element(by=By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/'
                                                                       'div/div[1]/div[1]/div/div[3]/div[5]/a/div/span')
        signin_button.click()

        sleep(3)

        email_address = self.webdriver.find_element(by=By.CSS_SELECTOR, value='input[name="text"]')
        email_address.send_keys(TWITTER_EMAIL, Keys.ENTER)

        password = self.webdriver.find_element(by=By.CSS_SELECTOR, value='input[name="password"]')
        password.send_keys(TWITTER_PASSWORD, Keys.ENTER)

        sleep(5)

        tweet_button_1 = self.webdriver.find_element(by=By.CSS_SELECTOR, value='a[aria-label="Tweet"]')
        tweet_button_1.click()

        sleep(3)

        tweet = self.webdriver.find_element(by=By.CSS_SELECTOR, value='div[data-contents="true"]')
        tweet.send_keys(f"Hey Internet Provider, why is my internet speed {self.download} Mbps down/{self.upload} Mbps "
                        f"up when I pay for {ISP_DOWNLOAD_SPEED}down/{ISP_UPLOAD_SPEED}up?")

        tweet_button_2 = self.webdriver.find_element(by=By.CSS_SELECTOR, value='div[data-testid="tweetButton"]')
        tweet_button_2.click()

        sleep(3)


twitter_bot = InternetSpeedTwitterBot()

twitter_bot.get_internet_speed()

if float(twitter_bot.download) < ISP_DOWNLOAD_SPEED or float(twitter_bot.upload) < ISP_UPLOAD_SPEED:
    twitter_bot.tweet_at_isp()

    with open("log.txt", "a") as log:
        log.write(f"\n{datetime.datetime.now()}: {twitter_bot.upload} Mbps Up, {twitter_bot.download} Mbps Down")
    print("Message Sent!")

    sleep(10)
    twitter_bot.webdriver.quit()
else:
    sleep(5)
    twitter_bot.webdriver.quit()



