Feature: Deleting a review


  Scenario: User deletes a review
         Given The site "http://127.0.0.1:5000" is opened
    Given The website "http://127.0.0.1:5000" is opened
    When The user clicks on the "movie" that choose
    When The user click on "delete review" button
    Then The number of reviews should decrease by 1
