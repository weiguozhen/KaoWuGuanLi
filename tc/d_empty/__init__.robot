*** Settings ***
Library  pylib.api.SchoolClassLib
Library  pylib.api.SchoolTeacherLib
Library  pylib.api.SchoolStudentLib
Suite Setup  Run Keywords
                            ...  delete_all_taeacher   AND
                            ...  delete_all_student  AND
                            ...  delete_all_classes
#添加学生需要指定班级的，所以学生依赖于班级，被依赖的要后删