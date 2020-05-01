#!/usr/bin/env python 
# -*- coding: utf-8 -*-

from robot.libraries.BuiltIn import BuiltIn
from pylib.api.util.handel_yaml import conf_read
from pylib.api.base import CommonRequests
from pprint import pprint
from robot.api import logger


class SchoolClassLib(CommonRequests):
    def __init__(self):
        CommonRequests.__init__(self)
        conf = conf_read()
        self.url = conf[conf['test_env']]['classUrl']
        self.vcode = conf[conf['test_env']]['vcode']

    def delete_classes(self, classid=3):
        url_join = f'{self.url}/{classid}'
        payload = {
            'vcode': self.vcode
        }
        response = self.request('delete', url_join, data=payload).json()
        pprint(response, indent=3)
        return response

    def delete_all_classes(self):

        data = self.list_classes()
        # pprint(data, indent=3)
        retlist = data['retlist']
        for _ in retlist:
            id = _['id']
            self.delete_classes(id)
        data = self.list_classes()
        pprint(data, indent=3)
        return data

    def list_classes(self, gradeid=None):
        if gradeid:
            payload = {
                'vcode': self.vcode,
                'action': 'list_classes_by_schoolgrade',
                'gradeid': gradeid
            }
        else:
            payload = {
                'vcode': self.vcode,
                'action': 'list_classes_by_schoolgrade',
            }
        response = self.request('get', url=self.url, data=payload)
        pprint(response.json(), indent=3)
        return response.json()

    def create_class(self, grade=2, name='111', count=80, idSavedName=None):
        payload = {
            "vcode": self.vcode,
            'action': 'add',
            'grade': int(grade),
            'name': name,
            'studentlimit': int(count)

        }
        response = self.request('post', self.url, data=payload).json()
        pprint(response)
        if idSavedName:
            print('before')
            BuiltIn().set_global_variable('${%s}' % idSavedName, response['id'])
            print(f'glocal var set: ${idSavedName}:{response["id"]}')
        return response

    def check_class_exist(self, data, name, grade__name, invitecode, studentlimit, studentnumber, id, desiredvalue=1):
        class_list = data['retlist']
        class_info = {
            'name': name,
            'grade__name': grade__name,
            'invitecode': invitecode,
            'studentlimit': int(studentlimit),
            'studentnumber': int(studentnumber),
            'id': id,
            "teacherlist": []
        }
        pprint(class_info)
        occurTimes = class_list.count(class_info)
        logger.info(f'occur {occurTimes} times')
        assert occurTimes == desiredvalue, f'班级列表包含了{occurTimes}次指定信息，期望包含{desiredvalue}次'

    def classlist_should_contain(self, classlist, classname, gradename, invitecode, studentlimit, studentnumber,
                                 classid, expectedtimes=2):
        item = {
            "name": classname,
            "grade__name": gradename,
            "invitecode": invitecode,
            "studentlimit": int(studentlimit),
            "studentnumber": int(studentnumber),
            "id": int(classid),
            "teacherlist": []
        }
        pprint(item)
        occurTimes = classlist['retlist'].count(item)
        logger.info('occur {} times'.format(occurTimes))

        if occurTimes != expectedtimes:
            raise Exception(
                'class list contain your class info {} times,expect {} times!!'.format(
                    occurTimes, expectedtimes)
            )

    def modif_class(self, id, name, count):
        base_url = f'{self.url}/{id}'
        payload = {
            'vcode': self.vcode,
            'action': 'modify',
            'name': name,
            'studentlimit': count
        }
        response = self.request('put', base_url, payload).json()
        pprint(response)
        return response


if __name__ == '__main__':
    SchoolClass = SchoolClassLib()
    # print(SchoolClass.list_classes(website))
    # SchoolClass.delete_all_classes()
    # SchoolClass.create_class(4,'2班',80)
    # SchoolClass.delete_classes(381524)
    # SchoolClass.create_class()
    # SchoolClass.modif_class('fafas', 89)

    # SchoolClass.delete_all_classes()
    for i in range(20):
        SchoolClass.create_class(4, f'{i+1}班', 80)
    SchoolClass.list_classes()
