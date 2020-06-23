from selenium import webdriver
from Locators import *
import time

driver = webdriver.Chrome('../chromedriver')

# Happy Path
driver.get('https://opensource-demo.orangehrmlive.com/')
username = driver.find_element(*LoginPage.username_field)
password = driver.find_element(*LoginPage.password_field)
submit = driver.find_element(*LoginPage.submit_btn)
username.send_keys('Admin')
password.send_keys('admin123')
submit.click()

time.sleep(2)

welcome_message = driver.find_element(*LoginPage.message)
print(welcome_message.text)
driver.quit()

# Sad Path
driver = webdriver.Chrome('../chromedriver')
driver.get('https://opensource-demo.orangehrmlive.com/')
username = driver.find_element(*LoginPage.username_field)
password = driver.find_element(*LoginPage.password_field)
submit = driver.find_element(*LoginPage.submit_btn)
username.send_keys('otheruser')
password.send_keys('123')
submit.click()

time.sleep(2)

sad_message = driver.find_element(*ForgetPassword.sad_message)
print(sad_message.text)

forgot_account_link = driver.find_element(*LoginPage.forget_password_link)
forgot_account_link.click()

time.sleep(2)

header = driver.find_element(*ForgetPassword.header)
print(header.text)

driver.quit()
