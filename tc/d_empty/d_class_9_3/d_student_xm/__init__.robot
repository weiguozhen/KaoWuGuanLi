*** Settings ***
Library  pylib.api.SchoolStudentLib
Library  pylib.web.web_pylib.PyLib
Variables  pylib/api/conf/conf.yaml
Suite Setup  run keywords  create_student  1527183103  小明  ${${test_env}.g_subject_science_id}    ${suiteclassid}  88888888   g_s_id  AND
            ...  openBrowser


Suite Teardown  run keywords  delete_student   ${g_s_id}  AND
    ...  quit