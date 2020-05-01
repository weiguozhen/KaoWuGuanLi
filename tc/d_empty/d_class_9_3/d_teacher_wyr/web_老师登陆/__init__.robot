*** Settings ***
Library  pylib.web.web_pylib.PyLib
Suite Setup  run keywords  openBrowser  AND  userLogin  15022615473  888888
Suite Teardown  quit
