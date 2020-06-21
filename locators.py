from selenium.webdriver.common.by import By

class Wikipedia(object):
    Random_Link = (By.CSS_SELECTOR, '#n-randompage')

class WikipediaArticle(object):
    First_Heading = (By.CSS_SELECTOR, '.firstHeading')
    Page_Info = (By.LINK_TEXT, 'Page information')
    Search_Info = (By.NAME, 'search')
    Logo = (By.XPATH, "/html//div[@id='p-logo']")