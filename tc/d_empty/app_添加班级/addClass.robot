*** Settings ***
Library  pylib.app.app_pylib.PyLib
Library  pylib.api.SchoolClassLib
*** Test Cases ***
tc006101
    ${a_c}  add_class  888班  1  88

    should be true  '添加成功' == $a_c[0]
    ${l_c}  list classes
    classlist_should_contain  ${l_c}  888班  七年级  ${a_c}[2]  88  0  ${a_c}[1]  1
    [Teardown]  delete classes  ${a_c}[1]