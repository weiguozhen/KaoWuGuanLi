#!/usr/bin/env python
# -*- coding: utf-8 -*-

from appium import webdriver
from pylib.app.util.handel_yaml import HandelYaml
from appium.webdriver.webdriver import WebDriver
from pylib.app.page.LoginPage import LoginPage

handel_yaml = HandelYaml()


class App:
    driver: WebDriver = None
    _server = handel_yaml.get_server()
    _wait = handel_yaml.conf_read('/Users/wgz/Desktop/考务管理系统/pylib/app/conf/mobile.yaml')['wait']
    _monitor = handel_yaml.conf_read('/Users/wgz/Desktop/考务管理系统/pylib/app/conf/mobile.yaml')['monitor']

    @classmethod
    def open(cls):
        cls.driver = webdriver.Remote(cls._monitor, cls._server)
        cls.driver.implicitly_wait(cls._wait)
        return LoginPage(cls.driver)

    @classmethod
    def quit(cls):
        cls.driver.quit()

    # 清除app登陆数据
    @classmethod
    def reset(cls):
        cls.driver.reset()
