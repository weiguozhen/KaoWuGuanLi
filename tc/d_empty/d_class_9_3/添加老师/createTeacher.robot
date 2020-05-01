*** Settings ***
Library  pylib.api.SchoolClassLib
Library  pylib.api.SchoolTeacherLib

*** Test Cases ***
tc001001
    [Tags]  老师
    ${ret1}  create class  3  333班  88

    ${ret2}  create teacher  xiaohong1  小红1  1  ${ret1['id']}  1231331321   123@qq.com   3209251983090987899
    should be true  $ret2['retcode'] == 0
    ${list}  teacher list
    check teacher exist  ${list}  xiaohong1  ${ret1['id']}  小红1    ${ret2['id']}  1231331321  123@qq.com  3209251983090987899
    [Teardown]  run keywords  delete teacher  ${ret2['id']}  AND
    ...  delete classes  &{ret1}[id]

