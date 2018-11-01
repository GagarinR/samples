__author__ = "Gagarin Ruslan"



import unittest

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions, Chrome, Firefox, FirefoxOptions, FirefoxProfile
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, TimeoutException, NoAlertPresentException
from selenium.webdriver.common.keys import Keys


class Selenium_GoogleSearchTest (unittest.TestCase):

    def explicitly_wait_for_element_by_xpath(self, element_xpath, timeout=15):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, element_xpath)))

        except (NoSuchElementException, TimeoutException):
            raise NoSuchElementException(
                'Element was not located by xpath "{}" within {} seconds'.format(element_xpath, timeout))

    def setUp(self):

        opts = Options()
        opts.add_experimental_option("detach", True)
        self.driver = Chrome(executable_path='chromedriver.exe', options=opts)

        '''We can create a POM for these elements, but this is a short task '''

        self.url = 'https://www.google.com/'
        self.search_bar = '//input[@title="Search"]'
        self.search_string = 'test automation is awesome'
        

    def test_testautomationisawesome(self):
        '''return the title of the search page result to console out.'''

        driver = self.driver

        driver.get(self.url)
        self.explicitly_wait_for_element_by_xpath(self.search_bar)
        driver.find_element_by_xpath(self.search_bar).send_keys(self.search_string)
        driver.find_element_by_xpath(self.search_bar).send_keys(Keys.RETURN)

        print(driver.title)





    def tearDown(self):
        '''remove env and delete files'''
        self.driver.quit()





