
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import unittest
from selenium.webdriver.common import desired_capabilities


class TestSearchForSelenium(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()


    def test_baidu(self):
        url = 'https://www.baidu.com'
        self.driver.get(url)
        self.driver.set_window_size(1167, 692)
        #time.sleep(5)
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.ID, "kw").click()
        self.driver.find_element(By.ID, "kw").send_keys("selenium")
        self.driver.find_element(By.ID, "kw").send_keys(Keys.ENTER)
        time.sleep(3)
        assert self.driver.title == "selenium_百度搜索"

    def tearDown(self):
        time.sleep(5)
        self.driver.quit()

if __name__ == "__main__":

    unittest.main()

