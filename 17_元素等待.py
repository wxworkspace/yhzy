"""

    selenium自动化中有几种元素等待的方式:
        显式等待:
            显示等待，就是明确的要等到某个元素的出现或者是某个元素的
            可点击等条件，等不到，就一直等，除非在规定的时间之内都没找到，
            那么抛出Exception(简而言之，就是直到元素出现才去操作，如果超时则报异常)

        隐式等待:
             针对全局，无指定元素，是设置了一个最长等待时间,
            如果在规定时间内网页加载完成,则执行下一步,
            否则一直等到时间截止,然后执行下一步. 一般会报错

            隐性等待对整个driver的周期都起作用，所以只要设置一次即可


    time模块中有sleep函数也可以进行等待,这种等待属于死等待,这种等待有时候会出现
    等死[线程抛出异常]的情况.

    隐性等待和显性等待可以同时用，但要注意：等待的最长时间取两者之中的大者



"""
import unittest

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait


class elwait(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.host = "http://127.0.0.1:8081"
    def test_elwait(self):
        self.driver.get(self.host+"/shop/registPage")
        WebDriverWait(self.driver,10).until(presence_of_element_located((By.ID,"username")))
        username = self.driver.find_element_by_id("username")
        username.click()
        username.clear()
        username.send_keys("haha")
        WebDriverWait(self.driver,10).until(presence_of_element_located((By.ID,"password")))
        password = self.driver.find_element_by_id("password")
        password.click()
        password.clear()
        password.send_keys("123")
        WebDriverWait(self.driver,10).until(presence_of_element_located((By.ID,"rePassword")))
        repassword = self.driver.find_element_by_id("rePassword")
        repassword.click()
        repassword.clear()
        repassword.send_keys("123")
        WebDriverWait(self.driver,10).until(presence_of_element_located((By.ID,"verifyCode")))
        veri = self.driver.find_element_by_id("verifyCode")
        veri.click()
        veri.send_keys("ABCD")
        WebDriverWait(self.driver,10).until(presence_of_element_located((By.CSS_SELECTOR,"#registerForm > table > tbody > tr:nth-child(11) > td > input")))
        su = self.driver.find_element_by_css_selector("#registerForm > table > tbody > tr:nth-child(11) > td > input")
        su.click()
        time.sleep(3)
        self.assertIn("恭喜您，注册成功",self.driver.page_source)
    def tearDown(self):
        self.driver.quit()
if __name__ == '__main__':
    unittest.main()