*** Settings ***
Library  pylib.api.SchoolClassLib
*** Test Cases ***
tc000002
    [Tags]  添加
    ${ret1}  create class  1  2班    90
    should be true  $ret1['retcode'] == 0
    ${ret2}  list classes
    ${invitecode}  evaluate  $ret1['invitecode']
    ${id}  evaluate  $ret1['id']
    check class exist  ${ret2}
    ...  2班  七年级  ${invitecode}  90  0   ${id}  1
    [Teardown]  delete_classes  ${ret1}[id]
tc000003
    [Tags]  添加
    ${listBefore}  list classes
    ${ret1}  create class  121223  1312221班  80
    should be true   $ret1['retcode'] == 1
    log  ${ret1}
    should be true  $ret1['reason'] == 'duplicated class name'
    ${listAfter}  list classes
    should be equal  ${listBefore}  ${listAfter}






