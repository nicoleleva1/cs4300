from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie, Seat, Booking
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer


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


# Shows the seats for one movie and lets you pick one
def seat_booking(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    all_seats = Seat.objects.all()

    # If the user submitted the form (POST request)
    if request.method == 'POST':
        chosen_seat_id = request.POST.get('seat_id')
        chosen_seat = get_object_or_404(Seat, id=chosen_seat_id)

        # Make the booking
        Booking.objects.create(movie=movie, seat=chosen_seat, user=request.user)

        # Mark the seat as booked so no one else can pick it
        chosen_seat.is_booked = True
        chosen_seat.save()

        return redirect('booking_history')

    return render(request, 'bookings/seat_booking.html', {'movie': movie, 'seats': all_seats})


# Shows the current user's past bookings
def booking_history(request):
    my_bookings = Booking.objects.filter(user=request.user)
    return render(request, 'bookings/booking_history.html', {'bookings': my_bookings})
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    
    # Free up the seat again
    booking.seat.is_booked = False
    booking.seat.save()
    
    # Delete the booking record
    booking.delete()
    
    return redirect('booking_history')
