import unittest

import time
from selenium import webdriver


class Kj(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.host = "http://127.0.0.1:8081"
    def test_kj(self):
        self.driver.get(self.host+"/SeleniumDemo/frameset.html")
        frameset = self.driver.find_element_by_tag_name("frameset")
        frame_list = frameset.find_elements_by_tag_name("frame")
        self.driver.switch_to.frame(frame_list[0])
        print(self.driver.find_element_by_id("div1").text)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame(frame_list[1])
        print(self.driver.find_element_by_tag_name("h2").text)

    def tearDown(self):
        time.sleep(2)
        self.driver.quit()
if __name__ == '__main__':
    unittest.main()