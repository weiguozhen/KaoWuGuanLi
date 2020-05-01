*** Settings ***
Library  pylib.app.app_pylib.PyLib
Suite Setup    openApp
Suite Teardown  closeApp
Test Setup  run keywords  reset  AND  login
Test Teardown  reset