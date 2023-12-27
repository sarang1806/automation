Feature: Guru 99 login
  Scenario: To verify guru99
    Given Open Chrome browser
    Given Enter the Guru99 site url
    Given Enter user Id and password with role "maneger"
    Then Click on login button
    Then Verify customer logged in successfully




#    Scenario Outline: To verify guru99 login page
#    Given Open Chrome browser
#    Given Enter the Guru99 site url
#    Given Enter user Id and password with role "<role>"
#    And Enter password
#    Then Click on login button
#    Then Verify customer logged in successfully


#      Examples: User credentials
#        |role|
#        |maneger|
#        |admin|
#        |user|