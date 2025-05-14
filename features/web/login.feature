Feature: Login to SauceDemo

  Scenario: User logs in with valid credentials
    Given the user opens the SauceDemo website
    When the user logs in with username "standard_user" and password "secret_sauce"
    Then the user should be redirected to the products page
