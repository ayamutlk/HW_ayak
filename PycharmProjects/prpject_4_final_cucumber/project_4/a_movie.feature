Feature: movie functional
#Feature: Test Top Button

#    Background: Open the movies website
#     Given The site "http://127.0.0.1:5000" is opened

  Scenario: Clicking the top button should scroll to the top of the page
    Given The website "http://127.0.0.1:5000" is open
    When I click on the "movie" from the homepage
    And I click on the "top button" in info page
    Then I should be scrolled to the top of the page





    Scenario: Clicking on the logo navigates to the About Me page
        Given Open the site "http://127.0.0.1:5000"
        When I click on the logo "about" from homepage up the page
        Then I am taken to the About Me page

  Scenario: Clicking on the logo image should navigate to the home page
      Given The site "http://127.0.0.1:5000" is open
      When The user clicks on the "movie" image
      And The user clicks on the "logo homepage"
      Then The user should be navigated to the home page


  Scenario Outline: User enters <status> login credentials
    Given The user is on the page url "http://127.0.0.1:5000"
    Then Click on "login"
    When The user enters <username> and <password>
    And The user clicks the "login button"
    Then The user should see an indication of login <status>

    Examples:
    | status | username | password |
    | incorrect | aya | password |
    | correct | aya | 123 |