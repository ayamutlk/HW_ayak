Feature: Update movie information



  Scenario Outline: Update a movie field
    Given the movie site "<url>" is opened
    When I click on the "movie" in the website
    And I click on the "alter button"
#    When Click on the "movie"
#    And Click on the "alter button"
    And I enter "<text>" as the box bar <field_name>
    And Click on the "update"
    Then I should see the new <field_name> on the page info movie

    Examples:
      | url                   | text                                     | field_name        |
      | http://127.0.0.1:5000 | Joseph Kosinski                          | director-alt      |
      | http://127.0.0.1:5000 | Cruise, Jennifer Connelly, Miles Teller  | main actors-alt   |
      | http://127.0.0.1:5000 | 2022                                     | release year-alt  |
