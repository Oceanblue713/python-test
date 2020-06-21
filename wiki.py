from selenium import webdriver
from locators import Wikipedia, WikipediaArticle
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('./chromedriver')
driver.get("https://en.wikipedia.org/")

# randam_link = driver.find_element_by_id('n-randompage')
randam_link = driver.find_element(*Wikipedia.Random_Link)
randam_link.click()

time.sleep(5)

first_heading = driver.find_element(*WikipediaArticle.First_Heading)
print(first_heading.text)

page_info = driver.find_element(*WikipediaArticle.Page_Info)
page_info.click()
time.sleep(5)

search_box = driver.find_element(*WikipediaArticle.Search_Info)
search_box.send_keys("Selenium (software)" + Keys.RETURN)
time.sleep(5)

Logo = driver.find_element(*WikipediaArticle.Logo)
Logo.click()
time.sleep(5)

driver.quit()
