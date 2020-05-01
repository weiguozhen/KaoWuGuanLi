#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import configparser
import sys
import os


class HandelIni:
    def load_ini(self):
        file_path = '/Users/wgz/Desktop/考务管理系统/pylib/app/conf/mobile.ini'
        cf = configparser.ConfigParser()
        cf.read(file_path, encoding='utf-8-sig')
        return cf

    def get_value(self, section='server1', key='name'):
        data = self.load_ini().get(section, key)
        return data

    def get_server(self, key):
        server = handelIni.get_value('server', 'server')
        return handelIni.get_value(server, key)


if __name__ == '__main__':
    handelIni = HandelIni()
    # print(handelIni.load_ini())
    print(handelIni.get_server('platformName'))
