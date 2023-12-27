from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import pandas as pd
from selenium.webdriver.common.keys import Keys


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
    except Exception:
        driver.execute_script("window.scrollBy(0, 500);")
        scroll_count += 1
        time.sleep(1)
#
# while scroll_count2 < 20:
#     inner_div = driver.find_element(By.XPATH, '//*[@id="simpleRegistryList"]')
#     driver.execute_script('arguments[0].scrollBy(0, 500)', inner_div, 500)
#     scroll_count2 += 1
#     time.sleep(1)

num_list = ['550001787', '550023956', '550000660', '550002484', '550001116', '550007432', '550007706', '550006570', '550008065', '550024191', '550024193', '550024549', '550024432', '550025038', '550023850', '550024421', '550024512', '550024980', '550025128', '550025471', '550025685', '550025613', '550025768', '550025780', '550025771', '550026036', '550026002', '550026260', '550002486', '550003766', '550003137', '550004381', '550018105', '550018107', '550018103', '550019109', '550018096', '550019778', '550018766', '550019873', '550020773', '550002504', '550002502', '550022662', '550022754', '550020929', '550002494', '550002497', '550022782', '550022779', '550022963', '550022814', '550023287', '550023282', '550023338', '550023278', '550023518', '550002498', '550002495', '550002499', '550022342', '550002496', '550022120', '550002500', '550002501', '550022399', '550023892', '550023905', '550024224', '550024548']
# objects = driver.find_elements(By.CLASS_NAME, 'display-inline-block')
# for obj in objects:
#     if len(obj.text) > 14:
#         num_list.append(obj.text.split('Порядковый номер в едином перечне классифицированных гостиниц')[1].split('Дата')[0])

input_field = driver.find_element(By.CSS_SELECTOR, '#lisensesWidget > licenses-widget > div > simple-registry > div.panel.panel-shadow.mb-20 > div > div:nth-child(3) > div:nth-child(1) > div > input')
submit_button = driver.find_element(By.CSS_SELECTOR, '#lisensesWidget > licenses-widget > div > simple-registry > div.panel.panel-shadow.mb-20 > div > div:nth-child(4) > div:nth-child(8) > div > button')
object_button = driver.find_element(By.CLASS_NAME, 'panel panel-shadow mb-10 cursor-pointer')
for num in num_list:
    input_field.clear()
    input_field.send_keys(num)
    input_field.send_keys(Keys.RETURN)
    time.sleep(1)
    submit_button.click()
    time.sleep(1)
    object_button.click()
    time.sleep(1000)

print(num_list)
driver.quit()
