Feature: Adding a comment to a review



  Scenario: User adds a comment to a review
    Given The site "http://127.0.0.1:5000" is opened
    Then Click on the "movie"
    When The user adds a "comment" with name
    And New "review text"
     And New "rating" stars
     And Click on the "rating button"
    Then The comment is added successfully

