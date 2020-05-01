*** Settings ***
Library  pylib.api.SchoolClassLib
*** Test Cases ***
tc000051

    [Tags]  修改22
    ${ret1}  create class  2  2班  80

    ${ret2}  modif class  ${ret1['id']}  3班  44
    should be true  $ret2['retcode'] == 0
    ${ret3}  list classes
    check_class_exist  ${ret3}
    ...  3班  八年级  ${ret1}[invitecode]  44  0  ${ret1}[id]  1
    [Teardown]  delete classes  ${ret1}[id]



tc000052
    [Tags]  修改

    ${ret1}  create class  122  33333班  80
    ${list2}  list classes
    check_class_exist  ${list2}
    ...  3班  七年级  ${ret1}[invitecode]   80  0  ${ret1}[id]  1

    ${ret2}  modif class  ${ret1['id']}  1班  44
    should be true  $ret2['retcode'] == 1
    should be true  $ret2['reason'] == duplicated class name
    log  ${ret2}
    ${list3}  list classes
    should be equal  ${list2}  ${list3}



tc000053
    [Tags]  修改
    ${ret1}  modif class  4444444  33班  88
    should be true  $ret1['retcode'] == 404
    should contain  ${ret1['reason']}  班级不存在






