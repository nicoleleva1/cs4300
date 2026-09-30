from django.urls import path, include
from rest_framework import routers
from . import views

# automatically builds the /api/ URLs 
router = routers.DefaultRouter()
router.register('movies', views.MovieViewSet)
router.register('seats', views.SeatViewSet)
router.register('bookings', views.BookingViewSet)


urlpatterns = [
    path('api/', include(router.urls)),

    # normal website pages
    path('', views.movie_list, name='movie_list'),
    path('book/<int:movie_id>/', views.seat_booking, name='seat_booking'),    path('history/', views.booking_history, name='booking_history'),

    path('cancel/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
]
