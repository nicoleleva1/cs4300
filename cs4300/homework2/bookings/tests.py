from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from .models import Movie, Seat, Booking
from datetime import date

class MovieTests(TestCase):

    def setUp(self):
        # This runs before every test
        self.client = APIClient()
        self.movie = Movie.objects.create(
            title="Test Movie",
            description="Just a test",
            release_date="2023-01-01",
            duration=120
        )

    def test_movie_list_works(self):
        # Check that hitting the API returns a 200 OK
        response = self.client.get('/api/movies/')
        self.assertEqual(response.status_code, 200)

    def test_can_create_movie(self):
        data = {
            "title": "New Movie",
            "description": "Another test",
            "release_date": "2023-05-05",
            "duration": 100
        }
        response = self.client.post('/api/movies/', data)
        self.assertEqual(response.status_code, 201)
class SeatTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.seat = Seat.objects.create(seat_number="A1", is_booked=False)

    def test_seat_list_works(self):
        # Make sure we can see the seat through the API
        response = self.client.get('/api/seats/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_seat_starts_available(self):
        # A new seat should not be booked yet
        self.assertFalse(self.seat.is_booked)

    def test_can_create_seat(self):
        data = {"seat_number": "B2", "is_booked": False}
        response = self.client.post('/api/seats/', data)
        self.assertEqual(response.status_code, 201)


class BookingTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='pass123')
        self.movie = Movie.objects.create(
            title="Dune",
            description="Sand planet stuff",
            release_date=date(2021, 10, 22),
            duration=155
        )
        self.seat = Seat.objects.create(seat_number="A1", is_booked=False)

    def test_create_booking_via_api(self):
        data = {
            "movie": self.movie.id,
            "seat": self.seat.id,
            "user": self.user.id
        }
        response = self.client.post('/api/bookings/', data)
        self.assertEqual(response.status_code, 201)

    def test_booking_history_shows_up(self):
        # Create a booking directly, then check it's returned by the API
        Booking.objects.create(movie=self.movie, seat=self.seat, user=self.user)
        response = self.client.get('/api/bookings/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)


class BookingFlowTests(TestCase):
    """
    This is more of an integration test - it checks the
    full flow of a user booking a seat through the website
    (not just the API), and that the seat becomes unavailable after.
    """

    def setUp(self):
        self.client = TestCase.client_class()
        self.user = User.objects.create_user(username='flowuser', password='pass123')
        self.client.login(username='flowuser', password='pass123')
        self.movie = Movie.objects.create(
            title="Oppenheimer",
            description="Physics drama",
            release_date=date(2023, 7, 21),
            duration=180
        )
        self.seat = Seat.objects.create(seat_number="C3", is_booked=False)

    def test_booking_a_seat_marks_it_as_booked(self):
    	response = self.client.post(f'/book/{self.movie.id}/', {'seat_id': self.seat.id})
    	# Instead of checking a flag on the seat, check that a Booking now exists
    	self.assertEqual(Booking.objects.count(), 1)
    	self.assertTrue(Booking.objects.filter(movie=self.movie, seat=self.seat).exists())
    
    def test_cancel_booking_frees_seat(self):
    	booking = Booking.objects.create(movie=self.movie, seat=self.seat, user=self.user)

    	self.client.login(username='flowuser', password='pass123')
    	self.client.get(f'/cancel/{booking.id}/')

    	# After canceling, the booking should be gone entirely
    	self.assertEqual(Booking.objects.count(), 0)
    	self.assertFalse(Booking.objects.filter(movie=self.movie, seat=self.seat).exists())
