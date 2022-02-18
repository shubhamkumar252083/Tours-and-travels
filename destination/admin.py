from django.contrib import admin

# Register your models here.
from .models import *


class DestinationAdmin(admin.ModelAdmin):
    list_display = ("id", "country", "state", "city",
                    "place_name", "price", "discount_price",)
    search_fields = ("id", "state", "city", "place_name", "price",
                     "discount_price", "slug", "continent", "country")


class BookingAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "phone")
    search_fields = ("id", "name", "email", "phone", "address",
                     "location", "guests", "arrivals", "leaving")


class CustomerReviewAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "stars")
    search_fields = ("id", "name", "stars", "review")


admin.site.register(AboutUs)
admin.site.register(Destination, DestinationAdmin)
admin.site.register(Booking, BookingAdmin)
admin.site.register(CustomerReview, CustomerReviewAdmin)
