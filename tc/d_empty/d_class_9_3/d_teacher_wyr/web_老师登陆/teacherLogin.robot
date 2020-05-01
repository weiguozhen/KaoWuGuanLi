*** Settings ***
Library  pylib.web.web_pylib.PyLib
*** Test Cases ***
tc005001
    [Tags]  mainpage
    ${teacherinfo}  check_teacher_mainpage_info
    ${students}  check_classStatusPage
    should be true  $students == {'九年级3班':[]}
    should be true  $teacherinfo == ['松勤学院00914', '王怡然', '初中数学', '0', '0', '1']

