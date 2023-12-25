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

objects = driver.find_elements(By.CSS_SELECTOR, '#simpleRegistryList > div:nth-child(1) > div > div.mb-5.text-bold > div')
for obj in objects:
    print(obj.text)# for i in range(len(objects)):
#     # Scroll to the element using ActionChains
#     ActionChains(driver).move_to_element(objects[i]).perform()
#     time.sleep(1)
#
#     # Click on the element
#     objects[i].click()
#     time.sleep(3)
#
#     page_source = driver.page_source
#     soup = BeautifulSoup(page_source, 'html.parser')
#
#     data_divs = soup.find_all('div', class_='panel panel-shadow mb-10')
#
#     for data_div in data_divs:
#         hotel_name = data_div.find('h5').text.strip()
#         address = data_div.find('p', {'class': 'mb-5'}).text.strip()
#
#         data_list.append({'Hotel Name': hotel_name, 'Address': address})
#
#     back_button_xpath = '/html/body/div[1]/div[1]/div/div/div/div/div/div/div[2]/div/div/div/div/licenses-widget/div/simple-registry-record/div[1]/div/div/div/button'
#     back_button = driver.find_element(By.XPATH, back_button_xpath)
#     driver.execute_script("arguments[0].click();", back_button)
#
# df = pd.DataFrame(data_list)
#
# df.to_excel('hotel_data.xlsx', index=False)

driver.quit()
