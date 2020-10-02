"""
    1.访问百度的首页
    2.获取输入框元素 输入Python
    3.获取百度一下按钮元素 点击
    4.获取Python(计算机程序设计语言) - 百度百科链接  点击
    5.切换到新的窗口
    6.获取到百度百科的输入框 输入java
    7.获取进入词条按钮  点击按钮
"""
import unittest

import time
from selenium import webdriver


class Window(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.host = "http://www.baidu.com"
    def test_window(self):
        self.driver.get(self.host)
        kw = self.driver.find_element_by_id("kw")
        kw.click()
        kw.clear()
        kw.send_keys("python")
        su = self.driver.find_element_by_id("su")
        su.click()
        bdbk = self.driver.find_element_by_partial_link_text("百度百科")
        bdbk.click()
        # 获取新的窗口对象
        window = self.driver.window_handles[-1]
        self.driver.switch_to.window(window)
        kw1 = self.driver.find_element_by_id("query")
        kw1.click()
        kw1.clear()
        kw1.send_keys("Java")
        su2 = self.driver.find_element_by_id("search")
        su2.click()
    def tearDown(self):
        time.sleep(2)
        self.driver.quit()
if __name__ == '__main__':
    unittest.main()