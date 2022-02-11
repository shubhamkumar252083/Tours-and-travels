from django.urls import path

from .views import (HomeView, about, PackageView, booking, PlaceDetailView)

app_name = 'destination'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', about, name='about'),
    path('package/', PackageView.as_view(), name='package'),
    path('booking/', booking, name="booking"),
    path('<slug>/', PlaceDetailView.as_view(), name='place'),
]
