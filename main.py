from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import pandas as pd

driver = webdriver.Firefox()

url = "https://knd.gov.ru/simpleregistry"
driver.get(url)

max_scrolls = 500
scroll_count = 0
scroll_count2 = 0

while scroll_count < max_scrolls:
    try:
        link_to_hotels_registry = driver.find_element(By.XPATH,
                                                      '/html/body/div[1]/div[1]/div/div/div/div/div/div/div[2]/div/div/div/div/licenses-widget/div/simple-registries/div[2]/div[3]/div/p[1]/strong')
        driver.execute_script('arguments[0].scrollIntoView(true);', link_to_hotels_registry)
        link_to_hotels_registry.click()
        break
    except:
        driver.execute_script("window.scrollBy(0, 500);")
        scroll_count += 1
        time.sleep(1)

while scroll_count2 < 10:
    inner_div = driver.find_element(By.XPATH, '//*[@id="simpleRegistryList"]')
    driver.execute_script('arguments[0].scrollBy(0, 500)', inner_div, 500)
    scroll_count2 += 1
    time.sleep(1)

data_list = []
num_list = []
objects = driver.find_elements(By.CSS_SELECTOR, 'div.panel:nth-child(2) > div:nth-child(1) > div:nth-child(1)')
for obj in objects:
    print((obj.text).split('Порядковый номер в едином перечне классифицированных гостиниц')[1].split('Дата')[0])
driver.quit()
