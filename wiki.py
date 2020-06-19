from selenium import webdriver
from locators import Wikipedia
import time

driver = webdriver.Chrome('./chromedriver')
driver.get("https://en.wikipedia.org/")

# randam_link = driver.find_element_by_id('n-randompage')
randam_link = driver.find_element(*Wikipedia.Random_Link)
randam_link.click()

time.sleep(5)
print(driver.title)

driver.quit()
