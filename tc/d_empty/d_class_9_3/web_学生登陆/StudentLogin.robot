*** Settings ***
Library  pylib.web.web_pylib.PyLib
Library  pylib.api.SchoolStudentLib
Variables  pylib/api/conf/conf.yaml
*** Test Cases ***
tc005081
    ${ret1}  create_student  1527183103  张杰  ${${test_env}.g_subject_science_id}    ${suiteclassid}  88888888   g_s_id
    stuUserLogin  1527183103  888888  S
    ${c_s_m_i}  check_stu_mainpage_info
    should be true  $c_s_m_i == ['张杰', '松勤学院00914', '0', '0']
    ${c_s_w_q}  check_stu_WrongQuestion_info
    should be true  $c_s_w_q == '您尚未有错题入库哦'
    [Teardown]  delete_student   ${ret1['id']}
