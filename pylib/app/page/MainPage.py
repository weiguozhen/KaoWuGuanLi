#!/usr/bin/env python 
# -*- coding: utf-8 -*-


from pylib.app.page.Base import Base
from pylib.app.util.handel_yaml import HandelYaml

handel_yaml = HandelYaml().conf_read()
from pylib.app.page.TeacherPage import TeacherPage
from pylib.app.util.handel_re import handel_re

class MainPage(Base):
    _classpage = handel_yaml['ClassPage']['classpage']
    _flush = handel_yaml['ClassPage']['flush']
    _noclass = handel_yaml['ClassPage']['noclass']
    _info = handel_yaml['ClassPage']['info']
    _add = handel_yaml['ClassPage']['add']
    _classname = handel_yaml['ClassPage']['classname']
    _classid = handel_yaml['ClassPage']['classid']
    _count = handel_yaml['ClassPage']['count']
    _commit = handel_yaml['ClassPage']['commit']
    _checkinfo = handel_yaml['ClassPage']['checkinfo']
    _ok = handel_yaml['ClassPage']['ok']
    _classlist = handel_yaml['ClassPage']['classlist']
    _classinfo = handel_yaml['ClassPage']['classinfo']
    _TowOrThree = handel_yaml['ClassPage']['toworthree']
    def check_class_info(self):
        self.find_element_by_accessibility_id_click(self._classpage)
        self.find_element_by_accessibility_id_click(self._flush)
        noclass = self.find_element_by_accessibility_id(self._noclass).text
        return noclass

    def check_class_c_t_info(self):
        eles = self.find_elements(self._info)[1:3]
        list = []
        for ele in eles:
            data = ele.text.replace('\xa0', '').replace(' ', '')
            list.append(data)
        return list


        #下滑获取所有的班级
        # classlist = self.find_element_by_accessibility_id(self._classlist)
        # cl = []
        # while True:
        #     eles = classlist.find_elements_by_xpath(self._TowOrThree)
        #     # eles = classlist.find_elements_by_class_name(self._classinfo)
        #     flag = False
        #     for ele in eles:
        #         text = ele.text.replace(' ','').replace('\xa0', '')
        #         # if len(text) < 2:
        #         #     continue
        #         if text not in cl:
        #             cl.append(text)
        #             flag = True
        #     if flag == False:
        #         break
        #     self.swipe_up()
        # return cl





    def add_class(self, classname, classid, count):
        self.find_element_by_accessibility_id_click(self._classpage)
        self.find_element_by_accessibility_id_click(self._add)
        self.find_element_by_uiautomator_sendkeys(self._classname, classname)
        self.find_element_by_uiautomator_sendkeys(self._classid, classid)
        self.find_element_by_uiautomator_sendkeys(self._count, count)
        self.find_element_by_uiautomator_click(self._commit)
        info = self.find_elements(self._checkinfo)
        if info:
            data = info[0].text
            self.find_element_click(self._ok)
            return handel_re(data)
        return '添加失败'



    def to_teacher_page(self):
        return TeacherPage(self.driver)
