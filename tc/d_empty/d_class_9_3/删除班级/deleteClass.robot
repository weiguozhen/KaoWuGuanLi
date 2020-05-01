*** Settings ***
Library  pylib.api.SchoolClassLib

*** Test Cases ***
tc000081
    [Tags]  删除
    ${ret1}  delete classes   111
    log  ${ret1}
    should be true  $ret1['retcode'] == 404
    should contain  ${ret1['reason']}  班级不存在

tc000082
    [Tags]  删除
    ${ret1}  create class  1  222  80
    ${ret2}  delete classes  ${ret1['id']}
    ${ret3}  list classes
    should be true  $ret2['retcode'] == 0
    check_class_exist  ${ret3}
    ...  222  1  ${ret1}[invitecode]   80  0  ${ret1}[id]  0
