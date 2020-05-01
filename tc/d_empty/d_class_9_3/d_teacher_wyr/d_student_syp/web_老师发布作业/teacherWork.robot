*** Settings ***
Library  pylib.web.web_pylib.PyLib

*** Test Cases ***
tc005101
    openBrowser
    userLogin  15022615473  888888  T
    ${homework}  check_assign_homework
    should be true  '作业已发布给学生' in $homework


    stuUserLogin  1272235678  888888
    check_stu_homework_info


    userLogin  15022615473  888888
    ${c_s_h_i}  check_tea_homeworrk_info
    should be true  $c_s_h_i == ['A', 'A', 'A']
    quit
