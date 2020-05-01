#!/usr/bin/env python 
# -*- coding: utf-8 -*-

from time import sleep

from pylib.web.page.base import Base
from pylib.web.util.handel_yaml import HandelYaml
from pylib.web.page.StuWrongQuestion import StuWrongQuestion
from pylib.web.page.StuHomeWorkPage import StuHomeWorkPage

handel_yaml = HandelYaml()


class StuMainPage(Base):
    _wrongQuestion = handel_yaml.get_value('StuMainPage', 'wrongquestion')
    _info = handel_yaml.get_value('StuMainPage', 'info')
    _mainpage = handel_yaml.get_value('StuMainPage', 'mainpage')
    _homeworkpage = handel_yaml.get_value('StuMainPage', 'homeworkpage')
    _tohomework = handel_yaml.get_value('StuMainPage', 'tohomework')

    def to_wrong_question(self):
        self.find_element_click(self._wrongQuestion)
        return StuWrongQuestion(self.driver)

    def to_homework_page(self):
        print('xixi')
        self.find_element_click(self._homeworkpage)
        self.find_element_click(self._tohomework)
        return StuHomeWorkPage(self.driver)

    def check_stu_mainpage_info(self):
        self.find_element_click(self._mainpage)
        sleep(1)
        eles = self.find_elements(self._info)
        data = [ele.text for ele in eles]
        del data[2]
        return data

# ['张杰', '松勤学院00914', '0', '0']
