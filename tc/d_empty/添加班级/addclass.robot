*** Settings ***
Library  pylib.api.SchoolClassLib

*** Test Cases ***
tc000001
    [Tags]  添加
    ${ret1}  create class  1  xxxxx2222222xxx  90
    should be true  $ret1['retcode'] == 0
    ${ret2}  list classes
    ${fc}  evaluate  $ret2['retlist'][0]
    should be true  $fc['id']==$ret1['id']
    ${lsit}  list classes
    should be true  $fc['invitecode'] == $ret1['invitecode']
    [Teardown]  delete classes  ${ret1}[id]
