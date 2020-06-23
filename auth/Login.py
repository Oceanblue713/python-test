from selenium import webdriver
import time

driver = webdriver.Chrome('../chromedriver')

# Happy Path
driver.get('https://opensource-demo.orangehrmlive.com/')
username = driver.find_element('username')
password = driver.find_element('password')
submit = driver.find_element('submit')
username.send_keys('user')
password.send_keys('Admin123')
submit.click()

time.sleep(2)

welcome_message = driver.find_element('welcome_message')
print(welcome_message)