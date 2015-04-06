*** Settings ***
Library           Selenium2Library
Library           auto_twitter.TwitterAutoLibrary

*** Variables ***
${valid_username}    netsgr8_4us@yahoo.com
${valid_password}    thisispassword
${SERVER}         twitter.com
${BROWSER}        Firefox
${DELAY}          0
${LOGIN URL}      http://${SERVER}/
${WELCOME URL}    http://${SERVER}/welcome.html
${ERROR URL}      http://${SERVER}/error.html

*** Keywords ***
go to twitter and login
    Open Browser    ${LOGIN URL}    ${BROWSER}
    Login    ${valid_username}    ${valid_password}
