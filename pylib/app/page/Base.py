#!/usr/bin/env python 
# -*- coding: utf-8 -*-

from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pylib.app.util.handel_yaml import HandelYaml

handel_yaml = HandelYaml().conf_read('/Users/wgz/Desktop/考务管理系统/pylib/app/conf/BlackList.yaml')


class Base:
    _MainPagePopUp = handel_yaml['BlackList']['MainPagePopUp']
    _LoginPopUp = handel_yaml['BlackList']['LoginPopUp']

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def get_size(self):
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']
        return width, height

    def swipe_left(self):
        swipe = self.get_size()
        x1 = swipe[0] / 10 * 9
        y1 = swipe[1] / 2
        x = swipe[0] / 10
        print('向左滑动')
        self.driver.swipe(x1, y1, x, y1)

    def swipe_right(self):
        swipe = self.get_size()
        x1 = swipe[0] / 10
        y1 = swipe[1] / 2
        x = swipe[0] / 10 * 9
        print('向右滑动')
        self.driver.swipe(x1, y1, x, y1)

    def swipe_up(self):
        swipe = self.get_size()
        y = swipe[1] / 10 * 4
        y1 = swipe[1] / 10 * 8
        x1 = swipe[0] / 10 * 2
        print('向上滑动')
        self.driver.swipe(x1, y1, x1, y)

    def swipe_down(self):
        swipe = self.get_size()
        y = swipe[1] / 10 * 9
        y1 = swipe[1] / 10
        x1 = swipe[0] / 2
        print('向下滑动')
        self.driver.swipe(x1, y1, x1, y)

    def find_element_by_accessibility_id_click(self, locator):
        print(locator)
        try:
            self.driver.find_element_by_accessibility_id(locator).click()
        except:
            self.handle_exception()
            return self.driver.find_element_by_accessibility_id(locator).click()

    def find_element_by_accessibility_id(self, locator):
        print(locator)
        try:
            return self.driver.find_element_by_accessibility_id(locator)
        except:
            self.handle_exception()
            return self.driver.find_element_by_accessibility_id(locator)

    def find_element_by_uiautomator_click(self, locator):
        print(locator)
        try:
            return self.driver.find_element_by_android_uiautomator(locator).click()
        except:
            self.handle_exception()
            return self.driver.find_element_by_android_uiautomator(locator).click()
    def find_element_by_uiautomator_sendkeys(self, locator,text):
        print(locator)
        try:
            return self.driver.find_element_by_android_uiautomator(locator).send_keys(text)
        except:
            self.handle_exception()
            return self.driver.find_element_by_android_uiautomator(locator).send_keys(text)

    def find_element(self, locator):
        print(locator)
        try:
            return self.driver.find_element(*locator)
        except:
            self.handle_exception()
            return self.driver.find_element(*locator)

    def find_elements(self, locator):
        print(locator)
        try:
            return self.driver.find_elements(*locator)
        except:
            self.handle_exception()
            return self.driver.find_elements(*locator)

    def find_element_click(self, locator):
        print(locator)
        try:
            self.driver.find_element(*locator).click()
        except:
            self.handle_exception()
            self.driver.find_element(*locator).click()

    def send_keys(self, locator, text):
        print(locator)
        try:
            input_text = self.driver.find_element(*locator)
            input_text.clear()
            input_text.send_keys(text)
        except:
            self.handle_exception()
            input_text = self.driver.find_element(*locator)
            input_text.clear()
            input_text.send_keys(text)

    def get_toast(self, text=None, timeout=5, poll_frequency=0.5):
        """
        get toast
        :param text: toast text
        :param timeout: Number of seconds before timing out, By default, it is 5 second.
        :param poll_frequency: sleep interval between calls, By default, it is 0.5 second.
        :return: toast
        """
        if text:
            toast_loc = ("//*[contains(@text, '%s')]" % text)
        else:
            toast_loc = "//*[@class='android.widget.Toast']"

        try:
            WebDriverWait(self.driver, timeout, poll_frequency).until(
                EC.presence_of_element_located(('xpath', toast_loc)))
            toast_elm = self.driver.find_element_by_xpath(toast_loc)
            return toast_elm.text

        except:
            return "Toast not found"

    def handle_exception(self):
        print('exception')
        page_source = self.driver.page_source
        if 'image_cancle' in page_source:
            self.driver.find_element(*self._MainPagePopUp).click()
        elif 'tips' in page_source:
            self.driver.find_element(*self._LoginPopUp).click()
        else:
            raise Exception('异常处理未捕获，请检查网页元素')
# 向下滑动
# def down(self):
#     locator = self.driver.find_element(self._LoginPopUp).location
#     x1 = locator['x']
#     y1 = locator['y']-200
#     y2 = y1-300
#     self.driver.swipe(start_x=x1,end_x=x1,start_y=y1,end_y=y2)
