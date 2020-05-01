#*** Keywords ***
#suite setup action
#    ${ret}  create class  website  1班  60
#    set global variable  ${suite_classid}  &{ret}[id]
#
#*** Settings ***
#Library  pylib.SchoolClassLib
#Suite Setup   suite setup action
#Suite Teardown  delete_classes  ${suite_classid}

*** Settings ***
Library  pylib.api.SchoolClassLib
Suite Setup  create_class  3  3班  60  suiteclassid
Suite Teardown  delete_classes  ${suiteclassid}