#!/usr/bin/env python 
# -*- coding: utf-8 -*-


from robot.libraries.BuiltIn import BuiltIn
from pylib.api.SchoolClassLib import SchoolClassLib
from pylib.api.util.handel_yaml import conf_read
from pylib.api.base import CommonRequests
from pprint import pprint


class SchoolStudentLib(CommonRequests):
    def __init__(self):
        CommonRequests.__init__(self)
        conf = conf_read()
        self.url = conf[conf['test_env']]['studentUrl']
        self.vcode = conf[conf['test_env']]['vcode']

    def create_student(self, username, realname, gradeid, classid, phonenumber, g_s_id=None):
        payload = {
            'vcode': self.vcode,
            'action': 'add',
            'username': username,
            'realname': realname,
            'gradeid': gradeid,
            'classid': classid,
            'phonenumber': phonenumber
        }
        response = self.request('post', self.url, payload).json()
        pprint(payload)
        if g_s_id:
            BuiltIn().set_global_variable('${%s}' % g_s_id, response['id'])
        return response

    def modify_student(self, student_id, realname=None, phonenumber=None):
        baseurl = f'{self.url}/{student_id}'
        payload = {
            'vcode': self.vcode,
            'action': 'modify',
        }
        if realname:
            payload['realname'] = realname
        if phonenumber:
            payload['phonenumber'] = phonenumber
        response = self.request('put', baseurl, payload).json()
        pprint(response)
        return response

    def delete_student(self, student_id):
        baseurl = f'{self.url}/{student_id}'
        payload = {
            'vcode': self.vcode
        }
        response = self.request('delete', baseurl, payload).json()
        pprint(response)
        return response

    def list_student(self):
        payload = {
            'vcode': self.vcode,
            'action': 'search_with_pagenation'
        }
        response = self.request('get', self.url, payload).json()
        pprint(response)
        return response

    def delete_all_student(self):
        teacher_list = self.list_student()['retlist']
        for _ in teacher_list:
            teacher_id = _['id']
            self.delete_student(teacher_id)
        if self.list_student()['retlist'] != []:
            print('学生未清除完毕')

    def check_student_exists(self, classid, username, realname, phonenumber, id, expectedtimes=1):
        item = {
            "classid": int(classid),
            "username": username,
            "realname": realname,
            "phonenumber": phonenumber,
            "id": int(id)
        }
        pprint(item)
        student_list = self.list_student()['retlist']
        count = student_list.count(item)
        if count != int(expectedtimes):
            raise Exception(f'班级列表包含了{count}次指定信息,期望包含{expectedtimes}!!')


# [ { 'grade__name': '九年级',
# 'id': 383455,
# 'invitecode': '3834559698342',
# 'name': '3班',
# 'studentlimit': 60,
# 'studentnumber': 1,
# 'teacherlist': [ { 'subject__name': '初中数学',
#                    'subject_id': 1,
#                    'teacher__realname': '小红333',
#                    'teacher__user_id': 173579}]}]}


if __name__ == '__main__':
    student = SchoolStudentLib()
    classes = SchoolClassLib()
    # response = classes.create_class(2, '3222班', 80)
    # response1 = student.create_student('b', '莉莉',3, '383867', '185168202311')
    # student.modify_student(response1['id'], '李世民', '1882724298126')
    # sleep(5)
    # student.delete_all_student()
    # student.check_student_exists(response['id'], '1232325', '李世民', '1882724298126', response1['id'])
    student.list_student()
    # student.delete_all_student()
