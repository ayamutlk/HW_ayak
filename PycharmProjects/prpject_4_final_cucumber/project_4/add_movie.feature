Feature: Test functionality



  Scenario: Add new movie to my website
    Given Open web application
    Then Count "img" in the "beginning"
    Then click on log in logo
    Then put the username and put the password
    When Navigate to add movie button
    And Add data to "movie_title"
    And Add data to "director"
    And Add data to "release_year"
    And Add data to "description"
    And Add data to "poster"
    And Add data to "actor"
    And Add data to "video"
    And Click on ADD button
    Given Open web application
    Then Count "img" in the "end"
    Then Validate end is bigger than beginning

#  Scenario Outline: Alter movie data
#    Given Open web application
#    When Navigate to movie detail URL
#    And Click on ALTER button
#    And Add data to "<indicator>"
#    And Click on SUBMIT button
#    Then Validate content in "<indicator>"
#
#    Examples:
#      | indicator    |
#      | movie_title  |
#      | director     |
#      | release_year |
#      | description  |
#
