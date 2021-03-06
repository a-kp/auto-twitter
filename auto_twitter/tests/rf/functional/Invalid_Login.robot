*** Settings ***
Documentation     A test suite containing tests related to invalid login.
...
...               These tests are data-driven by their nature. They use a single
...               keyword, specified with Test Template setting, that is called
...               with different arguments to cover different scenarios.
...
...               This suite also demonstrates using setups and teardowns in
...               different levels.
Suite Setup       Open Browser    https://twitter.com    browser=${BROWSER}
Suite Teardown    Close Browser
Test Setup        go to    https://twitter.com
Test Teardown     Take Screenshot

Test Template     Login
Library           auto_twitter.TwitterAutoLibrary
Library           Selenium2Library
Library           Screenshot
Resource          resource.robot

*** Test Cases ***    User Name            Password             Fail
Invalid Username      invalid              ${valid_password}    ${True}

Invalid Password      ${valid_username}    invalid              ${True}

Invalid Username And Password
                      invalid              whatever             ${True}

Empty Username        ${EMPTY}             ${valid_password}    ${True}

Empty Password        ${valid_username}    ${EMPTY}             ${True}

Empty Username And Password
                      ${EMPTY}             ${EMPTY}             ${EMPTY}

*** Keywords ***
