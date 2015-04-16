*** Settings ***
Suite Setup       go to twitter and login
Suite Teardown    close browser
Resource          resource.robot
Library           FakerLibrary

*** Test Cases ***
retweet 10
    Retweet    10
