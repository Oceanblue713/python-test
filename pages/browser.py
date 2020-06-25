from selenium import webdriver

class Browser(object):

    base_url = "https://opensource-demo.orangehrmlive.com/"
    opts = webdriver.ChromeOptions()
    opts.add_experimental_option("detach", True)
    driver = webdriver.Chrome('../chromedriver', chrome_options=opts)

    def find_element(self, *Locator):
        return self.driver.find_element(*Locator)

    def quit(self):
        self.driver.quit()

    def visit(self, Location=''):
        url = self.base_url + Location
        self.driver.get(url)