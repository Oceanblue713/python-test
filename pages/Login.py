from pages.browser import Browser
from selenium import webdriver
from Locators import *
import time

class LoginPage(Browser):

    def __init__(self):
        self.LOGIN = '/'

    def Log_in_as(self, username, password):
        self.visit(self.LOGIN)
        username_field = self.find_element(*LoginPageLocators.username_field)
        password_field = self.find_element(*LoginPageLocators.password_field)
        submit_btn = self.find_element(*LoginPageLocators.submit_btn)
        username_field.send_keys(username)
        password_field.send_keys(password)
        submit_btn.click()
        time.sleep(2)

    def get_auth_message(self):
        return self.find_element(*LoginPageLocators.message)

    def click_forgotpassword_link(self):
        forgatpassword_link = self.find_element(*LoginPageLocators.forget_password_link)
        forgatpassword_link.click()
        time.sleep(2)

    def get_page_header(self):
        return self.find_element(*ForgetPasswordLocators.header)