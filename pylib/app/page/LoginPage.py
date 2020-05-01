#!/usr/bin/env python 
# -*- coding: utf-8 -*-

from pylib.app.page.Base import Base
from pylib.app.page.MainPage import MainPage
from pylib.app.util.handel_yaml import HandelYaml

handel_yaml = HandelYaml().conf_read()


class LoginPage(Base):
    _vcode = HandelYaml().conf_read('/Users/wgz/Desktop/考务管理系统/pylib/app/conf/mobile.yaml')['vcode']
    _inputText = handel_yaml['LoginPage']['inputtext']
    _login = handel_yaml['LoginPage']['login']
    _errorinfo = handel_yaml['LoginPage']['errorinfo']

    def login(self):
        self.send_keys(self._inputText, self._vcode)
        self.find_element_click(self._login)
        return MainPage(self.driver)

    def login_error(self, text):
        self.send_keys(self._inputText, text)
        self.find_element_click(self._login)

        exist = self.find_elements(self._errorinfo)
        if exist:
            # print(self.find_element(self._errorinfo).text)
            errorInfo = exist[0].text
            return errorInfo
        return 'vcode 输入正确，请输入错误vcode'
