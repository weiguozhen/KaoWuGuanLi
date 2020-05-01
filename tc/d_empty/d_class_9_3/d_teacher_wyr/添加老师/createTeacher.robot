*** Settings ***
Library  pylib.api.SchoolClassLib
Library  pylib.api.SchoolTeacherLib

*** Test Cases ***
tc001002
    [Tags]  老师
    ${ret1}  create class  3  9班  88

    ${ret2}  create teacher  laoli  老李  1  ${ret1['id']}  122231331321   123@qq.com   32092251983090987899
    should be true  $ret2['retcode'] == 0
    ${list}  teacher list
    check teacher exist  ${list}  laoli  ${ret1['id']}  老李  ${ret2['id']}  122231331321  123@qq.com  32092251983090987899
    [Teardown]  run keywords  delete teacher  ${ret2['id']}   AND
    ...  delete_classes  ${ret1}[id]

tc001003
    [Tags]  老师
    ${r_t_l_1}  teacher list
    ${r_c_t}  create teacher  15022615473  jjj  2  ${suiteclassid}  122231331321   123@qq.com   32092251983090987899
    should be true  $r_c_t['retcode'] == 1
    should be true  $r_c_t['reason'] == u"登录名 15022615473 已经存在"
    ${r_t_l_2}  teacher list
    should be equal  ${r_t_l_1}  ${r_t_l_2}
tc001051
    [Tags]  老师
    ${r_t_l_1}  teacher list
    ${r_m_t}  modify_teacher  1111
    should be true  $r_m_t['retcode'] == 1
    should contain  ${r_m_t}[reason]   老师不存在
    ${r_t_l_2}  teacher list
    should be equal  ${r_t_l_1}  ${r_t_l_2}
#tc001052
#    [Tags]  老师1
#    ${list}  list classes
#
#
#    ${ret1}  create class  website  93333班  88
#    ${r_c_t}  create teacher  laoli  老李  website  ${ret1['id']}  122231331321   123@qq.com   32092251983090987899
#    ${r_m_t}  modify_teacher  ${r_c_t}[id]  realname=huahua  subjectid=website  classlist=&{ret1}[id],${suiteclassid}
#    should be true  $r_m_t['retcode'] == 0
#    ${r_t_l_1}  teacher list
#    check teacher exist  ${r_t_l_1}  xiaohong333   ${ret1}[id],${suiteclassid}   huahua  ${global_teacher_id}  12313321   123@qq.com   32092519887899
#    [Teardown]  delete_classes  ${ret1}[id]
tc001081
    [Tags]  老师
    ${r_d_t}  delete_teacher  8088
    should be true  $r_d_t['retcode'] == 404
    log to console  ${r_d_t}
    should be true  $r_d_t['reason'] == u"id 为`8088`的老师不存在"
tc001082
    [Tags]  老师
    ${list}  list classes
    ${list1}  teacher list
    ${ret1}  create class  3  9班  88
    ${ret2}  create teacher  laoli  老李  1  ${ret1['id']}  122231331321   123@qq.com   32092251983090987899
    should be true  $ret2['retcode'] == 0
    delete teacher  ${ret2['id']}
    ${list2}  teacher list
    should be true  ${list1} == ${list2}
    [Teardown]  delete_classes  ${ret1}[id]


