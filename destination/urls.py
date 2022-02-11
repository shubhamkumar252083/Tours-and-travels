from django.urls import path

from .views import (HomeView, AboutView, PackageView, booking, PlaceDetailView)

app_name = 'destination'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('package/', PackageView.as_view(), name='package'),
    path('booking/', booking, name="booking"),
    path('<slug>/', PlaceDetailView.as_view(), name='place'),
]
