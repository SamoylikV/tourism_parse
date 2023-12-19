from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

driver = webdriver.Firefox()

url = "https://knd.gov.ru/simpleregistry"

driver.get(url)

max_scrolls = 10
scroll_count = 0

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

time.sleep(5)

objects = driver.find_elements(By.XPATH,
                               '/html/body/div[1]/div[1]/div/div/div/div/div/div/div[2]/div/div/div/div/licenses-widget/div/simple-registry/div[2]/div[1]/div')

for obj in objects:
    obj.click()

    time.sleep(3)

    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')
    back_button_xpath = '/html/body/div[1]/div[1]/div/div/div/div/div/div/div[2]/div/div/div/div/licenses-widget/div/simple-registry-record/div[1]/div/div/div/button'
    back_button = driver.find_element(By.XPATH, back_button_xpath)
    driver.execute_script("arguments[0].click();", back_button)

    time.sleep(3)

driver.quit()
