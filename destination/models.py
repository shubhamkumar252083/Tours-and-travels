
from django.db import models
from django.shortcuts import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
from django_countries.fields import CountryField

# Create your models here.

CONTINENT_CHOICES = (
    ('as', 'Asia'),
    ('af', 'Africa'),
    ('na', 'North America'),
    ('sa', 'South America'),
    ('an', 'Antarctica'),
    ('eu', 'Europe'),
    ('au', 'Australia')
)


class AboutUs(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text


class Destination(models.Model):
    continent = models.CharField(
        choices=CONTINENT_CHOICES, max_length=2, default="as")
    country = CountryField(multiple=False, default="IN")
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=50)
    place_name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    description_of_place = models.TextField()
    description_of_package = models.TextField()
    img_main = models.ImageField()
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    treanding = models.BooleanField(default=False)
    img1 = models.ImageField()
    img2 = models.ImageField()
    img3 = models.ImageField()
    img4 = models.ImageField()
    img5 = models.ImageField()

    def __str__(self):
        return self.country.name

    def get_absolute_url(self):
        return reverse("destination:place", kwargs={
            'slug': self.slug
        })


class Booking(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.IntegerField(

        validators=[MaxValueValidator(
            9999999999), MinValueValidator(6666666666)]
    )
    address = models.CharField(max_length=500)
    location = models.CharField(max_length=500)
    guests = models.PositiveSmallIntegerField(default=1)
    arrivals = models.DateField()
    leaving = models.DateField()
