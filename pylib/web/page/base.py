#!/usr/bin/env python 
# -*- coding: utf-8 -*-

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.select import Select

# from pylib.web.page.main_page import LoginPage
from pylib.web.util.handel_yaml import HandelYaml

handel_yaml = HandelYaml()


class Base:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find_element(self, locator):
        print(locator)
        try:
            return self.driver.find_element(*locator)
        except:
            self.handel_exception()
            return self.driver.find_element(*locator)

    def send_keys(self, locator, text):
        print(locator)
        try:
            input_text = self.driver.find_element(*locator)
            input_text.clear()
            input_text.send_keys(text)
        except:
            self.handel_exception()
            input_text = self.driver.find_element(*locator)
            input_text.clear()
            input_text.send_keys(text)

    def find_elements(self, locator):
        print(locator)
        try:
            return self.driver.find_elements(*locator)
        except:
            self.handel_exception()
            return self.driver.find_elements(*locator)

    def find_element_click(self, locator):
        print(locator)
        try:
            self.driver.find_element(*locator).click()
        except:
            self.handel_exception()
            return self.driver.find_element(*locator).click()

    def find_select(self, locator, text):
        ele = Select(self.find_element(locator))
        ele.select_by_visible_text(text)

    def find_web_element(self, webele, locator):
        try:
            return webele.find_element(*locator)
        except:
            self.handel_exception()
            return webele.find_element(*locator)

    def find_web_element_click(self, webele, locator):
        try:
            return webele.find_element(*locator).click()
        except:
            self.handel_exception()
            return webele.find_element(*locator).click()

    def find_web_elements(self, webele, locator):
        try:
            return webele.find_elements(*locator)
        except:
            self.handel_exception()
            return webele.find_elements(*locator)

    def web_send_keys(self, webele, locator, text):
        try:
            ele = webele.find_element(*locator)
            ele.clear()
            ele.send_keys(text)
        except:
            self.handel_exception()
            ele = webele.find_element(*locator)
            ele.clear()
            ele.send_keys(text)

    def handel_exception(self):
        print('exceptiion')
        black_list = handel_yaml.get_value('blacklist', 'except', '../conf/BlackList.yaml')
        self.driver.implicitly_wait(0)
        for locator in black_list:
            print(locator)
            try:
                self.driver.find_element(*locator).click()
            except:
                print(f'{str(locator)} not found')
        self.driver.implicitly_wait(10)
