*** Settings ***
Library  pylib.api.SchoolClassLib
Library  pylib.api.SchoolTeacherLib
Library  pylib.api.SchoolStudentLib
Variables  pylib/api/conf/conf.yaml
*** Test Cases ***
haha
    [Tags]  haha
    log to console     ${${test_env}.vcode}
    log to console     &{server1}[classUrl]
    log to console     ${${test_env}.g_subject_math_id}
    ${list1}  list student
    ${list2}  list classes
    ${list3}  teacher list

#robot -P . -v test_env:server --test haha tc
