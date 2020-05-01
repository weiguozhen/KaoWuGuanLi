#!/usr/bin/env python 
# -*- coding: utf-8 -*-

from time import sleep

from pylib.web.page.base import Base
from pylib.web.page.ClassStatusPage import ClassStatusPage
from pylib.web.util.handel_yaml import HandelYaml
from pylib.web.page.HomeWorkPage import HomeWorkPage

handel_yaml = HandelYaml()


class MainPage(Base):
    _classStatus = handel_yaml.get_value('MainPage', 'classstatus')
    _classStudent = handel_yaml.get_value('MainPage', 'classstudent')
    _checkTeacherInfo = handel_yaml.get_value('MainPage', 'checkteacherinfo')
    _mainpage = handel_yaml.get_value('MainPage', "mainpage")
    _homeWorkPage = handel_yaml.get_value('HomeWorkPage', 'homeworkpage')

    def to_class_status(self):
        self.find_element_click(self._classStatus)
        self.find_element_click(self._classStudent)
        return ClassStatusPage(self.driver)

    def to_homework_page(self):
        self.find_element_click(self._homeWorkPage)
        return HomeWorkPage(self.driver)

    def check_teacher_mainpage_info(self):
        self.find_element_click(self._mainpage)
        sleep(1)
        data = self.find_elements(self._checkTeacherInfo)
        teacher_info = [_.text for _ in data]
        return teacher_info
