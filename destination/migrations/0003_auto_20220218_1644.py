# Generated by Django 3.2 on 2022-02-18 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destination', '0002_customerreview'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='img6',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='destination',
            name='img7',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='destination',
            name='img8',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]