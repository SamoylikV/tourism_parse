from selenium import webdriver
from selenium.webdriver.common.by import By
import time

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

while scroll_count2 < 100:
    inner_div = driver.find_element(By.XPATH,
                        '//*[@id="simpleRegistryList"]')
    driver.execute_script('arguments[0].scrollBy(0, 500)', inner_div, 500)
    scroll_count2 += 1
    time.sleep(1)

objects = driver.find_elements(By.CSS_SELECTOR, 'div.panel-body')

print(objects)

# for i in range(len(objects)):
#     objects[i].click()
#
#     time.sleep(3)
#     #print(f"Processing object {i + 1}:\n{driver.page_source}")
#
#     back_button_xpath = '/html/body/div[1]/div[1]/div/div/div/div/div/div/div[2]/div/div/div/div/licenses-widget/div/simple-registry-record/div[1]/div/div/div/button'
#     back_button = driver.find_element(By.XPATH, back_button_xpath)
#     driver.execute_script("arguments[0].click();", back_button)
#
#     time.sleep(3)

# Close the browser after use
driver.quit()
