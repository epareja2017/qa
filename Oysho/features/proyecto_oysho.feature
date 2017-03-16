Feature: Proyecto Oysho 
    Análisis de la utilidad de esta herramienta en el entorno de QA.

  @Sprint1
  Scenario: Visit Home Page (uid:bf1b12b2-4c61-4c76-a3c4-3072450680ed)
    Given the user opens "http://google.es"
    When the user searches for "Oysho"
    Then the title should be "Oysho"

  @Sprint1
  Scenario Outline: Sign In Workflow (uid:18abb8b6-781d-4ab8-a5a9-ff24762674ea)
    Given a user that wants to register on "http://www.oysho.es"
    When the user credentials are introduced  "newuser@gmail.com" "10/02/2001" "Hola1234"
    Then the user is registered

    Examples:
      | user_email       | birth_date       | password       | hiptest-uid |
      | newtest@gmail.com | 10/02/2001 | Hola1234 | uid:cedf3432-af90-460c-b9cd-8abce08b0c84 |
