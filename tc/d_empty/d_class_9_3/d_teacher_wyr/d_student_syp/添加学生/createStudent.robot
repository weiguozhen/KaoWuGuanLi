*** Settings ***
Library  pylib.api.SchoolClassLib
Library  pylib.api.SchoolTeacherLib
Library  pylib.api.SchoolStudentLib
Variables  pylib/api/conf/conf.yaml
*** Test Cases ***
tc002002
    [Tags]  学生
    ${r_c_s}  create student  0988990  张无忌  ${${test_env}.g_subject_science_id}   ${suiteclassid}  185168202311
    should be true  $r_c_s['retcode'] == 0
    check student exists  ${suiteclassid}  0988990  张无忌  185168202311  &{r_c_s}[id]
    [Teardown]  delete student  &{r_c_s}[id]
tc002081
    [Tags]  学生1
    ${r_c_s}  create student  0323298890  张无忌  ${${test_env}.g_subject_science_id}   ${suiteclassid}  185168202311
    ${r_d_s}  delete student  ${r_c_s}[id]
    should be true  $r_d_s['retcode'] == 0
