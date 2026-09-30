from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie, Seat, Booking
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer
from django.contrib.auth.models import User

#  API VIEWS (for /api/ endpoints)
class MovieViewSet(viewsets.ModelViewSet):
    # This gives us list, create, update, delete for free
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer



# the website visual  part

# Shows all the movies
def movie_list(request):
    all_movies = Movie.objects.all()
    return render(request, 'bookings/movie_list.html', {'movies': all_movies})

def get_guest_user():
    # Everyone who isn't logged in shares this one "Guest" account
    guest, created = User.objects.get_or_create(username='guest')
    return guest

def seat_booking(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    all_seats = Seat.objects.all()

    booked_seat_ids = Booking.objects.filter(movie=movie).values_list('seat_id', flat=True)

    if request.method == 'POST':
        chosen_seat_id = request.POST.get('seat_id')
        chosen_seat = get_object_or_404(Seat, id=chosen_seat_id)

        # Use the logged-in user if there is one, otherwise fall back to a shared guest account
        current_user = request.user if request.user.is_authenticated else get_guest_user()

        Booking.objects.create(movie=movie, seat=chosen_seat, user=current_user)

        return redirect('booking_history')

    return render(request, 'bookings/seat_booking.html', {
        'movie': movie,
        'seats': all_seats,
        'booked_seat_ids': booked_seat_ids,
    })




# Shows the current user's past bookings
def booking_history(request):
    current_user = request.user if request.user.is_authenticated else get_guest_user()
    my_bookings = Booking.objects.filter(user=current_user)
    return render(request, 'bookings/booking_history.html', {'bookings': my_bookings})

def cancel_booking(request, booking_id):
    current_user = request.user if request.user.is_authenticated else get_guest_user()
    booking = get_object_or_404(Booking, id=booking_id, user=current_user)
    booking.delete()
    return redirect('booking_history')


from django.contrib.auth.models import User
from django.http import HttpResponse

def create_superuser_temp(request):
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'password')
        return HttpResponse("Superuser created successfully.")
    return HttpResponse("Superuser already exists.")
