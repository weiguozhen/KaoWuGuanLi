*** Settings ***
Library  pylib.api.SchoolClassLib
Library  pylib.api.SchoolTeacherLib
Library  pylib.api.SchoolStudentLib
Variables  pylib/api/conf/conf.yaml
*** Test Cases ***
tc002001
    [Tags]  学生111
    ${r_c_s}  create_student  12332122  苏无朋  ${${test_env}.g_subject_science_id}   ${suiteclassid}  185168202311
    should be true  $r_c_s['retcode'] == 0
    check student exists   ${suiteclassid}  12332122  苏无朋  185168202311  &{r_c_s}[id]
    [Teardown]  delete student  ${r_c_s['id']}



