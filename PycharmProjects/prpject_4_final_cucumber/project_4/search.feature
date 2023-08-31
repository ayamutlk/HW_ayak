# Scenario Outline
Feature: Search Functionality



Scenario Outline: Search functionality with different search terms
    Given The user is on the home page
    When The user enters "<search_term>" in the search field
    And Clicks the search button
    Then The search results page should be displayed

    Examples:
      | search_term       |
      | toy story         |
      | TOY STORY         |
      | nonexistent term  |
