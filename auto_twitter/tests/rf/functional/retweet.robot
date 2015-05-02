*** Settings ***
Suite Setup       go to twitter and login
Suite Teardown    close browser
Resource          resource.robot
Library           FakerLibrary

*** Test Cases ***
retweet 1
    Retweet    1

retweet 5
    Retweet    5
