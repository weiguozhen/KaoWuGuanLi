*** Settings ***
Library  pylib.api.SchoolStudentLib
Variables  pylib/api/conf/conf.yaml
Suite Setup  create_student  1272235678  苏有朋  ${${test_env}.g_subject_science_id}    ${suiteclassid}   18516998228202311  g_s_id
Suite Teardown  delete_student   ${g_s_id}