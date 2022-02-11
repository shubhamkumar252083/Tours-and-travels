# Generated by Django 3.2 on 2022-02-11 04:57

import django.core.validators
from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField(validators=[django.core.validators.MaxValueValidator(9999999999), django.core.validators.MinValueValidator(6666666666)])),
                ('address', models.CharField(max_length=500)),
                ('location', models.CharField(max_length=500)),
                ('guests', models.PositiveSmallIntegerField(default=1)),
                ('arrivals', models.DateField()),
                ('leaving', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('continent', models.CharField(choices=[('as', 'Asia'), ('af', 'Africa'), ('na', 'North America'), ('sa', 'South America'), ('an', 'Antarctica'), ('eu', 'Europe'), ('au', 'Australia')], default='as', max_length=2)),
                ('country', django_countries.fields.CountryField(default='IN', max_length=2)),
                ('state', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=50)),
                ('place_name', models.CharField(max_length=50)),
                ('slug', models.SlugField(unique=True)),
                ('description_of_place', models.TextField()),
                ('description_of_package', models.TextField()),
                ('img_main', models.ImageField(upload_to='')),
                ('price', models.FloatField()),
                ('discount_price', models.FloatField(blank=True, null=True)),
                ('treanding', models.BooleanField(default=False)),
                ('img1', models.ImageField(upload_to='')),
                ('img2', models.ImageField(upload_to='')),
                ('img3', models.ImageField(upload_to='')),
                ('img4', models.ImageField(upload_to='')),
                ('img5', models.ImageField(upload_to='')),
            ],
        ),
    ]
