#!/usr/bin/env python 
# -*- coding: utf-8 -*-



from pylib.app.page.Base import Base
from pylib.app.util.handel_yaml import HandelYaml
handel_yaml = HandelYaml().conf_read()
from pylib.app.util.handel_re import handel_teacher_re
class TeacherPage(Base):
    _refresh = handel_yaml['TeacherPage']['refresh']
    _noteacher = handel_yaml['TeacherPage']['noteacher']
    _teacherpage = handel_yaml["TeacherPage"]['teacherpage']
    _info = handel_yaml['TeacherPage']["info"]
    _add =handel_yaml['TeacherPage']["add"]
    _realnam =handel_yaml['TeacherPage']["realname"]
    _username =handel_yaml['TeacherPage']["username"]
    _subjectid =handel_yaml['TeacherPage']["subjectid"]
    _classlist =handel_yaml['TeacherPage']["classlist"]
    _phonenumber =handel_yaml['TeacherPage']["phonenumber"]
    _email =handel_yaml['TeacherPage']["email"]
    _idcardnumber =handel_yaml['TeacherPage']["idcardnumber"]
    _submit = handel_yaml['TeacherPage']["submit"]
    _okinfo =handel_yaml['TeacherPage']["okinfo"]
    _ok = handel_yaml['TeacherPage']['ok']
    _goback = handel_yaml['TeacherPage']['goback']
    _teacherinfo = handel_yaml['TeacherPage']['teacherinfo']
    def check_teacher_info(self):
        self.find_element_by_accessibility_id_click(self._teacherpage)
        self.find_element_by_accessibility_id_click(self._refresh)
        noteacher = self.find_element_by_accessibility_id(self._noteacher).text
        return noteacher

    def check_teacher_c_t_info(self):
        self.find_element_by_accessibility_id_click(self._teacherpage)
        eles = self.find_elements(self._info)[1:3]
        list = []
        for ele in eles:
            data = ele.text.replace('\xa0', '').replace(' ','')
            list.append(data)
        return list

    def add_teacher(self,realname,username,subjectid,classlist,phonenumber,email,idcardnumber,goback=True):
        self.find_element_by_accessibility_id_click(self._teacherpage)
        self.find_element_by_accessibility_id_click(self._add)
        self.find_element_by_uiautomator_sendkeys(self._realnam,realname)
        # self.send_keys(self._realnam,realname)
        self.find_element_by_uiautomator_sendkeys(self._username,username)
        self.find_element_by_uiautomator_sendkeys(self._subjectid,subjectid)
        self.find_element_by_uiautomator_sendkeys(self._classlist,classlist)
        self.find_element_by_uiautomator_sendkeys(self._phonenumber,phonenumber)
        self.find_element_by_uiautomator_sendkeys(self._email,email)
        self.find_element_by_uiautomator_sendkeys(self._idcardnumber,idcardnumber)
        self.find_element_by_uiautomator_click(self._submit)
        info = self.find_elements(self._okinfo)
        if info:

            data = handel_teacher_re(info[0].text)
            print(data)
            self.find_element_click(self._ok)
            if goback:
                self.find_element_by_uiautomator_click(self._goback)
                self.find_element_by_accessibility_id_click(self._teacherpage)
                eles = self.find_elements(self._teacherinfo)[1:3]
                list = []
                for ele in eles:
                    text = ele.text.replace('\xa0', '').replace(' ', '')
                    list.append(text)
                return list,data
            return data
        return '老师添加失败'










