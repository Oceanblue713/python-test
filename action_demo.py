from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("./chromedriver")
driver.get('https://google.com')

search_box = driver.find_element_by_name('q')
time.sleep(5)

search_box.send_keys("Seleniumhq" + Keys.RETURN)
time.sleep(10)

print(driver.title)

driver.quit()