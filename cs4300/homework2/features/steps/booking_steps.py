from behave import given, when, then
from bookings.models import Movie, Seat, Booking
from django.contrib.auth.models import User
from datetime import date


@given('there is a movie called "{title}"')
def step_create_movie(context, title):
    context.movie = Movie.objects.create(
        title=title,
        description="Test description",
        release_date=date(2023, 1, 1),
        duration=120
    )


@given('there is an available seat "{seat_number}"')
def step_create_seat(context, seat_number):
    context.seat = Seat.objects.create(seat_number=seat_number, is_booked=False)


@when('I visit the movie list page')
def step_visit_movie_list(context):
    context.response = context.test.client.get('/')


@then('I should see "{text}" on the page')
def step_check_text_on_page(context, text):
    content = context.response.content.decode()
    assert text in content, f'"{text}" was not found on the page'


@when('I book seat "{seat_number}" for "{title}"')
def step_book_seat(context, seat_number, title):
    context.user = User.objects.create_user(username='behaveuser', password='pass123')
    context.test.client.login(username='behaveuser', password='pass123')
    context.test.client.post(f'/book/{context.movie.id}/', {'seat_id': context.seat.id})


@then('the seat "{seat_number}" should be marked as booked')
def step_check_seat_booked(context, seat_number):
    from bookings.models import Booking
    assert Booking.objects.filter(movie=context.movie, seat=context.seat).exists()
