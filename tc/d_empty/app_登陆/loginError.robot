*** Settings ***
Library  pylib.app.app_pylib.PyLib
Suite Setup  openApp
Suite Teardown  closeApp
Test Setup  reset
Test Teardown  reset
*** Test Cases ***
tc006001
    ${errorinfo}  login error  xxxx
    should be true  $errorinfo == '登录失败 : vcode format error:1'
tc006002
    login
    ${c_c_i}  check_class_info
    ${c_t_i}  check_teacher_info
    should be true  $c_c_i == '该学校还没有班级，点击刷新'
