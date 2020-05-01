*** Settings ***
Library  pylib.app.app_pylib.PyLib
Suite Setup  openApp
Suite Teardown  closeApp
Test Setup  reset
Test Teardown  reset
*** Test Cases ***
tc006003
    login
    ${c_c_i}  check_class_c_t_info
    ${c_t_i}  check_teacher_c_t_info
    should be true  $c_c_i == ['九年级:3班', f'id：{${suiteclassid}}学生人数：0人数上限：60']
    should be true  $c_t_i == ['王怡然', f'id：{${global_teacher_id}}登录名：15022615473手机：5201314邮箱：123@qq.com身份证：0000000000']

