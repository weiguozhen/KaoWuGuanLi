#!/usr/bin/env python 
# -*- coding: utf-8 -*-


import configparser

class HandelIni:
    def load_ini(self):
        file_path = '/Users/wgz/Desktop/考务管理系统/pylib/web/conf/browser.ini'
        cf = configparser.ConfigParser()
        cf.read(file_path,encoding='utf-8-sig')
        return cf
    def get_value(self,section='browser',key='name'):
        data = self.load_ini().get(section,key)
        return data
    def get_login_url(self,flag):
        if 'S' in flag:
            url = 'student_login_url'
        elif 'T' in flag:
            url = 'teacher_login_url'
        else:
            return flag

        data = self.load_ini().get('url',url)
        return data
if __name__ == '__main__':
    handelIni = HandelIni()
    # print(handelIni.load_ini())
    print(handelIni.get_login_url('Teacher'))
