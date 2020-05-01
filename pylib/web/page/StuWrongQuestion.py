#!/usr/bin/env python 
# -*- coding: utf-8 -*-

from time import sleep

from pylib.web.page.base import Base
from pylib.web.util.handel_yaml import HandelYaml

handel_yaml = HandelYaml()


class StuWrongQuestion(Base):
    _info = handel_yaml.get_value('StuWrongQuestion', 'info')

    def check_WrongQuestion_info(self):
        sleep(1)
        return self.find_element(self._info).text
# 您尚未有错题入库哦
