from selenium import webdriver
from Locators import *
import time
import unittest

class LoginTestCase(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome('../chromedriver')
        self.addCleanup(self.browser.quit)

    def test_userLogin(self):
        self.browser.get('https://opensource-demo.orangehrmlive.com/')
        username = self.browser.find_element(*LoginPage.username_field)
        password = self.browser.find_element(*LoginPage.password_field)
        submit = self.browser.find_element(*LoginPage.submit_btn)

        username.send_keys('Admin')
        password.send_keys('admin123')
        submit.click()

        time.sleep(2)
        welcome_message = self.browser.find_element(*LoginPage.message)
        self.assertIn('Welcome Admin', welcome_message.text)

    def test_loginFail(self):
        self.browser.get('https://opensource-demo.orangehrmlive.com/')
        username = self.browser.find_element(*LoginPage.username_field)
        password = self.browser.find_element(*LoginPage.password_field)
        submit = self.browser.find_element(*LoginPage.submit_btn)

        username.send_keys('otheruser')
        password.send_keys('123')
        submit.click()

        time.sleep(2)
        sad_message = self.browser.find_element(*ForgetPassword.sad_message)
        self.assertIn('Invalid credentials', sad_message.text)

if __name__ == '__main__':
    unittest.main(verbosity=2)
