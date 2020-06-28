from selenium import webdriver
from pages.Login import LoginPage
import unittest

class LoginTestCase(unittest.TestCase):

    def test_userLogin(self):
        self.login_page = LoginPage()
        user = 'Admin'
        password = 'admin123'
        self.login_page.Log_in_as(user, password)
        welcome_message = self.login_page.get_auth_message()
        self.assertIn('Welcome Admin', welcome_message.text)

    def test_loginFail(self):
        self.login_page = LoginPage()
        user = 'abc'
        password = '123'
        self.login_page.Log_in_as(user, password)

        sad_message = self.login_page.get_auth_message()
        self.assertIn('Invalid credentials', sad_message.text)


if __name__ == '__main__':
    unittest.main(verbosity=2)
