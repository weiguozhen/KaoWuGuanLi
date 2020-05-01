*** Settings ***
Library  pylib.web.web_pylib.PyLib
Library  pylib.api.SchoolTeacherLib
Variables  pylib/api/conf/conf.yaml
*** Test Cases ***
tc005002
    ${r_c_t}  create teacher  1272235678  李思思  ${${test_env}.g_subject_math_id}  ${suiteclassid}  1314   123@qq.com  520
    userLogin   1272235678  888888  T

    ${c_t_m_i}  check_teacher_mainpage_info
    ${c_c_s_p}  check_classStatusPage
    should be true  $c_t_m_i == ['松勤学院00914', '李思思', '初中数学', '0', '0', '0']
    should be true  $c_c_s_p == {'九年级3班': ['小明']}
    [Teardown]  delete teacher  ${r_c_t['id']}


