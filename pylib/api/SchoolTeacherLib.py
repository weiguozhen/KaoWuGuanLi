#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import json
from pprint import pprint

from robot.api import logger
from pylib.api.util.handel_yaml import conf_read

from pylib.api.base import CommonRequests
from pylib.api.SchoolClassLib import SchoolClassLib
from robot.libraries.BuiltIn import BuiltIn


class SchoolTeacherLib(CommonRequests):
    def __init__(self):
        CommonRequests.__init__(self)
        conf = conf_read()
        self.url = conf[conf['test_env']]['teacherUrl']
        self.vcode = conf[conf['test_env']]['vcode']

    def create_teacher(self, username, realname, subjectid, classlist, phonenumber, email, idcardnumber,
                       global_id=None):
        tmpList = str(classlist).split(',')
        newclasslist = [{'id': oneid} for oneid in tmpList if oneid != '']

        payload = {
            'vcode': self.vcode,
            'action': 'add',
            'username': username,
            'realname': realname,
            'subjectid': int(subjectid),
            'classlist': json.dumps(newclasslist),
            'phonenumber': phonenumber,
            'email': email,
            'idcardnumber': idcardnumber
        }
        response = self.request('post', self.url, payload).json()
        pprint(response)
        if global_id:
            print('before')
            BuiltIn().set_global_variable('${%s}' % global_id, response['id'])
            print(f'glocal var set: ${global_id}:{response["id"]}')
        return response

    def teacher_list(self, subjectid=None):
        payload = {
            'vcode': self.vcode,
            'action': 'search_with_pagenation',
        }
        if subjectid:
            payload['subjectid']: subjectid

        response = self.request('get', self.url, payload).json()
        pprint(response)
        return response

    def modify_teacher(self, teacher_id, realname=None, subjectid=None, classlist=None, phonenumber=None, email=None,
                       idcardnumber=None):
        baseurl = f'{self.url}/{teacher_id}'
        payload = {
            'vcode': self.vcode,
            'action': 'modify'
        }
        classids = str(classlist).split(',')
        classidlist = [{'id': int(id)} for id in classids if id != '' and id != 'None']
        if realname:
            payload['realname'] = realname
        if subjectid:
            payload['subjectid'] = subjectid
        if classlist:
            payload['classlist'] = json.dumps(classidlist)
        if phonenumber:
            payload['phonenumber'] = phonenumber
        if email:
            payload['email'] = email
        if idcardnumber:
            payload['idcardnumber'] = idcardnumber
        pprint(payload)
        response = self.request('put', baseurl, payload).json()
        pprint(response)
        return response

    def check_teacher_exist(self, data, username, teachclasslist, realname, id, phonenumber, email, idcardnumber,
                            desiredvalue=1):
        teacher_list = data['retlist']
        classlist = [int(i) for i in str(teachclasslist).strip().split(',') if i != '']
        item = {
            "username": username,
            "teachclasslist": classlist,
            "realname": realname,
            "id": id,
            "phonenumber": phonenumber,
            "email": email,
            "idcardnumber": idcardnumber

        }
        pprint(item)
        count = teacher_list.count(item)
        logger.info(f'occur {count} times')
        assert count == desiredvalue, f'教师列表包含了{count}次指定信息，期望包含{desiredvalue}次'

    def delete_teacher(self, teacher_id):
        baseurl = f'{self.url}/{teacher_id}'
        payload = {
            'vcode': self.vcode
        }
        response = self.request('delete', baseurl, payload).json()
        pprint(response)
        return response

    def delete_all_taeacher(self):
        data = self.teacher_list()['retlist']
        for one in data:
            teacher_id = one['id']
            self.delete_teacher(teacher_id)
        self.teacher_list()


# { 'grade__name': '九年级',
# 'id': 383867,
# 'invitecode': '3838679273979',
# 'name': '2班',
# 'studentlimit': 80,
# 'studentnumber': 0,
# 'teacherlist': []}]}


if __name__ == '__main__':
    classes = SchoolClassLib()
    #
    # response = classes.create_class(3,'11班',88)
    # ret_id = response['id']
    # response = classes.create_class(website, 'fsaaf222fdfdfwffff', 88)
    # ret_id1 = response['id']
    # # #
    # # classlist =
    # #

    teacher = SchoolTeacherLib()

    # teacher.delete_teacher(381523)
    # teacher.delete_all_taeacher()
    # teacher.teacher_list()
    # teacher.create_teacher('1272235678','李世民',website,ret_id,'123231133121','123213@qq.com','323122219899')

    #
    # # data = teacher.teacher_list()
    # teacher.modify_teacher('115528',realname='王小二',subjectid=1,classlist='383455,383867')
    # # teacher.check_teacher_exist(data,'lishimfdsfin2',381290,'李世民2',114688,'12231331321','123@qq.com','32092510987899')
    teacher.teacher_list()
    # teacher.delete_teacher('114636')
    # teacher.teacher_list()
