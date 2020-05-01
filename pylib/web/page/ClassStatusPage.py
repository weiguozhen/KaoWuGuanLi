#!/usr/bin/env python 
# -*- coding: utf-8 -*-


# 第一种
# [
#     {
#         'name':'xxx1班',
#         'students':['s1','s2']
#     },
#      {
#         'name':'xxx2班',
#         'students':['s1','s2']
#     },
#
# ]

# 第二种
# {
#     'xxx1班':['s1','s2'],
#       'xxx2班':['s1','s2']
# }
from time import sleep

from pylib.web.util.handel_yaml import HandelYaml

handel_yaml = HandelYaml()

from pylib.web.page.base import Base
from pylib.web.util.handel_re import remove_count


class ClassStatusPage(Base):
    _classList = handel_yaml.get_value('ClassStatusPage', 'classlist')
    _title = handel_yaml.get_value('ClassStatusPage', 'title')
    _name = handel_yaml.get_value('ClassStatusPage', 'name')

    def click_class_student(self):
        self.class_list = self.find_elements(self._classList)
        for ele in self.class_list:
            self.find_web_element_click(ele, self._title)
            sleep(1)
        return self

    def check_teacher_statuspage_info(self):
        inner_dict = {}
        self.driver.implicitly_wait(0)
        for ele in self.class_list:
            title = remove_count(self.find_web_element(ele, self._title).text.replace(' ', ''))
            names = self.find_web_elements(ele, self._name)
            inner_list = [name.text for name in names]
            inner_dict[title] = inner_list
        self.driver.implicitly_wait(10)
        return inner_dict
