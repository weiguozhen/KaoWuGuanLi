*** Settings ***
Library  pylib.api.SchoolTeacherLib
Suite Setup  create_teacher  15022615473  王怡然  1  ${suiteclassid}  5201314   123@qq.com   0000000000  global_teacher_id
Suite Teardown    delete_teacher  ${global_teacher_id}
