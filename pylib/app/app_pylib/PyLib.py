#!/usr/bin/env python 
# -*- coding: utf-8 -*-

from pylib.app.page.App import App

app = App()


class PyLib:
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def openApp(self):
        self.openApp = app.open()

    def login(self):
        self.mainpage = self.openApp.login()

    def login_error(self, info):
        return self.openApp.login_error(info)

    def check_class_info(self):
        return self.mainpage.check_class_info()

    def check_teacher_info(self):
        return self.mainpage.to_teacher_page().check_teacher_info()

    def check_class_c_t_info(self):
        return self.mainpage.check_class_c_t_info()

    def check_teacher_c_t_info(self):
        return self.mainpage.to_teacher_page().check_teacher_c_t_info()

    def add_class(self, classname, classid, count):
        return self.mainpage.add_class(classname, classid, count)

    def add_teacher(self, realname, username, subjectid, classlist, phonenumber, email, idcardnumber,goback=True):
        return self.mainpage.to_teacher_page().add_teacher(realname, username, subjectid, classlist, phonenumber, email,
                                                           idcardnumber,goback)

    def reset(self):
        app.reset()

    def closeApp(self):
        app.quit()


if __name__ == '__main__':
    a = PyLib()

    a.openApp()
    a.reset()
    a.login()
    # print(a.add_teacher())
    print(a.add_class('xx',1,60))
    # print(a.add_teacher('fdsfs','ddd',1,387920,'3123131','313131','1231312312',False))
    # # print(a.check_class_c_t_info())
    # print(a.check_teacher_c_t_info())
    # print(a.check_class_info())
    # print(a.check_teacher_info())
    # print(a.login_error('xxxx'))
    # a = (['李玉妹', 'id：117301登录名：18516820311手机：15022615473邮箱：1272235678@qq.com身份证：88888888'], ('添加成功', '117301'))
    # print(a[1][1])
