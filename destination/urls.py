from django.urls import path

from .views import (HomeView, about, package, booking, PlaceDetailView)

app_name = 'destination'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', about, name='about'),
    path('package/', package, name='package'),
    path('booking/', booking, name="booking"),
    path('<slug>/', PlaceDetailView.as_view(), name='place'),
]
