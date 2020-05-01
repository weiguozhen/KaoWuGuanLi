*** Settings ***
Library  pylib.app.app_pylib.PyLib
Library  pylib.web.web_pylib.PyLib
Library  pylib.api.SchoolTeacherLib
Suite Setup  openApp
Suite Teardown  closeApp
Test Setup  reset
Test Teardown  run keywords  reset  AND   delete_teacher   ${a_t[1][1]}  AND   quit
*** Test Cases ***
tc006201
    login
    ${a_t}  add_teacher  李玉妹  18516820311  1  ${suiteclassid}  15022615473  1272235678@qq.com  88888888

    ${data}  evaluate  ['李玉妹', f'id：{${a_t[1][1]}}登录名：18516820311手机：15022615473邮箱：1272235678@qq.com身份证：88888888']
    should be equal  ${a_t[0]}   ${data}
    openBrowser
    userLogin  18516820311  888888  T
    ${c_t_m_i}  check_teacher_mainpage_info
    should be true   $c_t_m_i == ['松勤学院00914', '李玉妹', '初中数学', '0', '0', '0']
    ${students}  check_classStatusPage
    should be true  $students == {'九年级3班':[]}

