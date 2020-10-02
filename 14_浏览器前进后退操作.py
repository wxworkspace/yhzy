import unittest

import time
from selenium import webdriver


class BrowerDemo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.host = "http://www.baidu.com"
        self.host2 = "http://www.taobao.com"
    def test_brower(self):
        self.driver.get(self.host)
        self.driver.get(self.host2)
        self.driver.back()
        time.sleep(2)
        self.driver.forward()
    def tearDown(self):
        self.driver.quit()
if __name__ == '__main__':
    unittest.main()