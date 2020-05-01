#!/usr/bin/env python 
# -*- coding: utf-8 -*-


import yaml


class HandelYaml:
    def conf_read(self, conf_file):
        with open(conf_file) as f:
            file = f.read()
            conf = yaml.load(file, Loader=yaml.FullLoader)
            return conf

    def get_value(self, section, key, conf_file='/Users/wgz/Desktop/考务管理系统/pylib/web/conf/locator.yaml'):
        return self.conf_read(conf_file)[section][key]

    def get_switch_value(self, key, conf_file='/Users/wgz/Desktop/考务管理系统/pylib/web/conf/locator.yaml'):
        read = self.conf_read(conf_file)
        return read[read['switch_to']][key]


if __name__ == '__main__':
    # print(conf_read())
    a = HandelYaml()
    # print(a.conf_read())
    # print(a.get_value('TeacherLogin1','password'))
    print(a.get_switch_value('username'))
    # print(conf[conf['test_env']]['vcode'])
    # print(conf_read()[conf_read()['test_env']]['classUrl'])
