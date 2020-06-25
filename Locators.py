from selenium.webdriver.common.by import By

class LoginPageLocators(object):
    username_field = (By.CSS_SELECTOR, '#txtUsername')
    password_field = (By.CSS_SELECTOR, '#txtPassword')
    submit_btn = (By.NAME, 'Submit')
    forget_password_link = (By.LINK_TEXT, 'Forget your password?')
    message = (By.CSS_SELECTOR, '#welcome')

class ForgetPasswordLocators(object):
    sad_message = (By.CSS_SELECTOR, '#spanMessage')
    header = (By.TAG_NAME, 'h1')
