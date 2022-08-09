from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

web_service = Service(executable_path="C:\Development\chromedriver")
driver = webdriver.Chrome(service=web_service)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "cookie")
timeout = time.time() + 60*5
upgrades = []

for i in range(0, 1000000):
    cookie.click()
    values = driver.find_elements(By.CSS_SELECTOR, "#store b")
    for val in values:
        item = str(val.text)
        try:
            new_item = item.split("- ")[1]
            new_item = new_item.replace(",", "")
            upgrades.append(int(new_item))

        except IndexError:
            pass
    web_cookies = driver.find_element(By.ID, "money")
    latest_cookies = int(web_cookies.text)

    if latest_cookies >= upgrades[7]:
        button = driver.find_element(By.ID, "buyTime Machine")
        button.click()
    elif latest_cookies >= upgrades[6]:
        button = driver.find_element(By.ID, "buyPortal")
        button.click()
    elif latest_cookies >= upgrades[5]:
        button = driver.find_element(By.ID, "buyAlchemy lab")
        button.click()
    elif latest_cookies >= upgrades[4]:
        button = driver.find_element(By.ID, "buyShipment")
        button.click()
    elif latest_cookies >= upgrades[3]:
        button = driver.find_element(By.ID, "buyMine")
        button.click()
    elif latest_cookies >= upgrades[2]:
        button = driver.find_element(By.ID, "buyFactory")
        button.click()
    elif latest_cookies >= upgrades[1]:
        button = driver.find_element(By.ID, "buyGrandma")
        button.click()
    elif latest_cookies >= upgrades[0]:
        button = driver.find_element(By.ID, "buyCursor")
        button.click()

    upgrades = []

# for i in range(0, 1000000000):
#     cookie.click()
#     time.sleep(0.01)
#     while True:
#         time.sleep(60 - time.time() % 60)






driver.quit()