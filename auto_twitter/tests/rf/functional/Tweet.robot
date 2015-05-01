*** Settings ***
Suite Setup       go to twitter and login
Suite Teardown    close browser
Resource          resource.robot
Library           FakerLibrary

*** Test Cases ***
short tweet - below 10 characters
    ${tweet}    FakerLibrary.Text    10
    Tweet    ${tweet}

long tweet - below 140 characters
    ${tweet}    FakerLibrary.Text    135
    Tweet    ${tweet}

longer than allowed tweet - above
    ${tweet}    FakerLibrary.Text    500
    Tweet    ${tweet}
