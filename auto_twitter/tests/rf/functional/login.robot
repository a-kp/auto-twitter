*** Settings ***
Suite Teardown    close browser
Library           auto_twitter.TwitterAutoLibrary
Library           Selenium2Library
Resource          resource.robot

*** Test Cases ***
valid login
    Open Browser    https://twitter.com    ${BROWSER}
    Capture Page Screenshot
    Login    ${valid_username}    ${valid_password}
