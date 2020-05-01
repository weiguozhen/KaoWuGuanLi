#!/usr/bin/env python 
# -*- coding: utf-8 -*-


from pylib.web.page.base import Base
from pylib.web.util.handel_yaml import HandelYaml
from pylib.web.page.MainPage import MainPage
from pylib.web.util.handel_ini import HandelIni
from pylib.web.page.StuMainPage import StuMainPage

handel_yaml = HandelYaml()
handel_ini = HandelIni()


class LoginPage(Base):
    _usernameInput = handel_yaml.get_switch_value('username')
    _passwordInput = handel_yaml.get_switch_value('password')
    _usernameLocator = handel_yaml.get_value('LoginPage', 'username')
    _passwordLocator = handel_yaml.get_value('LoginPage', 'password')
    _loginbtnLocator = handel_yaml.get_value('LoginPage', 'loginbut')
    _checkEle = handel_yaml.get_value('LoginPage', 'checkele')

    def login(self, username=_usernameInput, password=_passwordInput, url="T"):
        base_url = handel_ini.get_login_url(url)
        self.driver.get(base_url)
        self.send_keys(self._usernameLocator, username)
        self.send_keys(self._passwordLocator, password)
        self.find_element_click(self._loginbtnLocator)
        return MainPage(self.driver), StuMainPage(self.driver)
