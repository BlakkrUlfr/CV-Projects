from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service

# from selenium.common.exceptions import StaleElementReferenceException
# from selenium.webdriver.common.keys import Keys

import time

chrome_driver_path = 'C:/Users/Admin/chromedriver.exe'
service = Service(executable_path=chrome_driver_path)
chromedriver = webdriver.Chrome(service=service)

chromedriver.get(url='http://orteil.dashnet.org/experiments/cookie/')

cookie = chromedriver.find_element(by=By.ID, value='cookie')

div_store = chromedriver.find_elements(by=By.CLASS_NAME, value='grayed')
store_ids = [upgrade.get_attribute(name='id') for upgrade in div_store]

timeout = time.time() + 300
interval = time.time() + 5

while time.time() < timeout:
    cookie.click()
    if time.time() >= interval:
        money = chromedriver.find_element(by=By.ID, value='money').text
        if ',' in money:
            money = money.replace(',', '')
        real_money = int(money)

        b_tags = chromedriver.find_elements(by=By.CSS_SELECTOR, value="#store div b")
        b_prices = [int(b_tag.text.split(sep='-')[1].strip().replace(',', '')) for b_tag in b_tags if b_tag.text != '']

        upgrades_cost_id = {b_prices[i]:store_ids[i] for i in range(len(b_prices))}

        affordable_upgrades = {cost:id for cost, id in upgrades_cost_id.items() if cost < real_money}

        most_expensive_affordable_upgrade = max(affordable_upgrades)
        purchased_upgrade_id = affordable_upgrades[most_expensive_affordable_upgrade]
        chromedriver.find_element(by=By.ID, value=purchased_upgrade_id).click()

        interval = time.time() + 5

cookies_per_secs = chromedriver.find_element(by=By.ID, value="cps").text
print(cookies_per_secs)

