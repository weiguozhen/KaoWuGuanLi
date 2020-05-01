#!/usr/bin/env python 
# -*- coding: utf-8 -*-

from robot.api import logger

from pylib.web.page.Web import Web

web = Web()


class PyLib:
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    # def __init__(self):
    #     logger.info('test_robot_library_scope',also_console=True)
    def openBrowser(self):
        self.openBrowser = web.start()

    def stuUserLogin(self, username, password, url='S'):
        self.stumainpage = self.openBrowser.login(username, password, url)[1]

    def userLogin(self, username, password, url='T'):
        self.mainpage = self.openBrowser.login(username, password, url)[0]

    def check_assign_homework(self):
        return self.mainpage.to_homework_page().create_homework('作业').assign_homework()

    def check_stu_mainpage_info(self):
        return self.stumainpage.check_stu_mainpage_info()

    def check_stu_WrongQuestion_info(self):
        return self.stumainpage.to_wrong_question().check_WrongQuestion_info()

    def check_teacher_mainpage_info(self):
        return self.mainpage.check_teacher_mainpage_info()

    def check_classStatusPage(self):
        return self.mainpage.to_class_status().click_class_student().check_teacher_statuspage_info()

    # 检查学生页面正确率，对错题
    def check_stu_homework_info(self):
        return self.stumainpage.to_homework_page().goto_homework().select_A()

    # 检查老师界面正确率，对错题
    def check_tea_homeworrk_info(self):
        return self.mainpage.to_homework_page().published_homework()

    def quit(self):
        web.quit()


if __name__ == '__main__':
    a = PyLib()
    a.openBrowser()
    a.userLogin('15022615473', '888888')
    print(a.check_assign_homework())
    a.quit()
    a = PyLib()
    a.openBrowser()
    a.stuUserLogin('1272235678', '888888')
    print(a.check_stu_homework_info())
    a.quit()
    a = PyLib()
    a.openBrowser()
    a.userLogin('15022615473', '888888')
    print(a.check_tea_homeworrk_info())
    # print(a.check_classStatusPage())
