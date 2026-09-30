Feature: Movie booking
    As a user
    I want to book a seat for a movie
    So that I can watch it

    Scenario: Viewing the movie list
        Given there is a movie called "Inception"
        When I visit the movie list page
        Then I should see "Inception" on the page

    Scenario: Booking an available seat
        Given there is a movie called "Inception"
        And there is an available seat "A1"
        When I book seat "A1" for "Inception"
        Then the seat "A1" should be marked as booked
