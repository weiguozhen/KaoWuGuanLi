#!/usr/bin/env python 
# -*- coding: utf-8 -*-

from time import sleep

from pylib.web.page.base import Base
from pylib.web.util.handel_yaml import HandelYaml

handel_yaml = HandelYaml()


class StuHomeWorkPage(Base):
    _goto = handel_yaml.get_value('StuHomeWorkPage', 'goto')
    _selectA = handel_yaml.get_value('StuHomeWorkPage', 'selectA')
    _submit = handel_yaml.get_value('StuHomeWorkPage', 'submit')
    _confirm = handel_yaml.get_value('StuHomeWorkPage', 'confirm')
    _clickimg = handel_yaml.get_value('StuHomeWorkPage', 'clickimg')
    _selecta = handel_yaml.get_value('StuHomeWorkPage', 'selecta')
    _pair = handel_yaml.get_value('StuHomeWorkPage', 'pair')
    _wrong = handel_yaml.get_value('StuHomeWorkPage', 'wrong')
    _accuracy = handel_yaml.get_value('StuHomeWorkPage', 'accuracy')

    def goto_homework(self):
        print('hahah')
        self.find_element_click(self._goto)
        sleep(1)
        return self

    def select_A(self):
        sleep(1)
        eles = self.find_elements(self._selectA)
        for _ in eles:
            self.find_web_element_click(_, self._selecta)
        self.find_element_click(self._submit)
        self.find_element_click(self._confirm)
        self.find_element_click(self._clickimg)
        pair = self.find_element(self._pair).text.replace(' ', '')
        wrong = self.find_element(self._wrong).text.replace(' ', '')
        accurracy = self.find_element(self._accuracy).text.replace(' ', '')
        data = f'{accurracy}:{pair}，{wrong}'
        return data
# 作业已发布给学生，任务编号为6213
# 正确率33%:对1题，错2题
