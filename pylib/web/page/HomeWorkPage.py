#!/usr/bin/env python 
# -*- coding: utf-8 -*-

from time import sleep

from pylib.web.page.base import Base
from pylib.web.util.handel_yaml import HandelYaml

handel_yaml = HandelYaml()


class HomeWorkPage(Base):
    _workname = handel_yaml.get_value('HomeWorkPage', 'workname')
    _selectTopic = handel_yaml.get_value('HomeWorkPage', 'selecttopic')
    _titleOption = handel_yaml.get_value('HomeWorkPage', 'titleoption')
    _topic = handel_yaml.get_value('HomeWorkPage', 'topic')
    _okbutton = handel_yaml.get_value('HomeWorkPage', 'okbutton')
    _btnsubmit = handel_yaml.get_value('HomeWorkPage', 'suretoadd')
    _message = handel_yaml.get_value('HomeWorkPage', 'message')
    _release = handel_yaml.get_value('HomeWorkPage', 'release')
    _issue = handel_yaml.get_value('HomeWorkPage', 'issue')
    _submit = handel_yaml.get_value('HomeWorkPage', 'submit')
    _btnprimary = handel_yaml.get_value('HomeWorkPage', 'btnprimary')
    _messageSubmit = handel_yaml.get_value('HomeWorkPage', 'messagesubmit')
    _createWork = handel_yaml.get_value('HomeWorkPage', 'creatework')
    _published = handel_yaml.get_value('HomeWorkPage', 'published')
    _statistics = handel_yaml.get_value('HomeWorkPage', 'statistics')
    _performance = handel_yaml.get_value('HomeWorkPage', 'performance')
    _look = handel_yaml.get_value('HomeWorkPage', 'look')
    _checkselect = handel_yaml.get_value('HomeWorkPage', 'checkselect')

    def create_homework(self, text):
        self.find_element_click(self._createWork)
        sleep(1)
        self.send_keys(self._workname, text)
        sleep(3)
        self.find_element_click(self._selectTopic)
        sleep(2)
        self.driver.switch_to.frame('pick_questions_frame')

        self.find_element_click(self._titleOption)
        sleep(2)
        eles = self.find_elements(self._topic)
        for index in range(3):
            eles[index].click()
        self.find_element_click(self._okbutton)
        sleep(2)
        self.driver.switch_to.default_content()
        self.find_element_click(self._btnsubmit)
        sleep(1)
        self.find_element_click(self._release)
        return self

    def assign_homework(self):
        main_window = self.driver.current_window_handle
        all_windows = self.driver.window_handles
        print(all_windows)
        for handel in all_windows:
            self.driver.switch_to.window(handel)
            if '下发学习任务' in self.driver.title:
                break
        sleep(1)
        self.find_element_click(self._issue)
        sleep(1)
        self.find_element_click(self._submit)
        sleep(1)
        self.find_element_click(self._btnprimary)
        sleep(1)
        data = self.find_element(self._message).text
        sleep(1)
        self.find_element_click(self._messageSubmit)
        self.driver.switch_to.window(main_window)
        return data

    def published_homework(self):
        self.find_element_click(self._published)
        self.find_element_click(self._performance)
        sleep(1)
        data = self.find_element(self._statistics).text.replace(' ', '')
        self.find_element_click(self._look)
        sleep(1)
        all_handles = self.driver.window_handles
        print(all_handles)
        for handel in all_handles:
            self.driver.switch_to.window(handel)
            if self.driver.title == '查看作业':
                break
        sleep(1)
        eles = self.find_elements(self._checkselect)
        sleep(1)
        content = [ele.find_element_by_xpath('./..').text.strip() for ele in eles]
        return content
