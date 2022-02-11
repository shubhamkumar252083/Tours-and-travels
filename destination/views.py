from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views import View
# Create your views here.
from .models import (Destination, Booking, AboutUs)
from .forms import BookingForm


def home(request):

    text_on_about_us_div = AboutUs.objects.last()

    context = {
        "text": text_on_about_us_div,
    }
    return render(request, "main/index.html", context)


class HomeView(ListView):
    model = Destination
    paginate_by = 8
    template_name = "main/index.html"
    # template_name = "try.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the AboutUs
        context['about'] = AboutUs.objects.last()

        return context


class PlaceDetailView(DetailView):
    model = Destination
    template_name = "try2.html"


def booking(request):
    form = BookingForm(request.POST or None)
    if form.is_valid():
        print(form.data)
        obj = Booking()
        obj.name = form.cleaned_data['name']
        obj.email = form.cleaned_data['email']
        obj.phone = form.cleaned_data['phone']
        obj.address = form.cleaned_data['address']
        obj.location = form.cleaned_data['location']
        obj.guests = form.cleaned_data['guests']
        obj.arrivals = form.cleaned_data['arrivals']
        obj.leaving = form.cleaned_data['leaving']
        # finally save the object in db
        obj.save()
        form = BookingForm()
        return HttpResponseRedirect('/')
    context = {
        'form': form
    }
    return render(request, "tryForm.html", context)


def package(request):

    return render(request, "test.html")


class PackageView(ListView):
    model = Destination
    paginate_by = 2
    template_name = "main/package.html"
    # template_name = "try.html"

    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get a context
    #     context = super().get_context_data(**kwargs)
    #     # Add in a QuerySet of all the AboutUs
    #     context['about'] = AboutUs.objects.last()
    #     return context


def about(request):

    return render(request, "test.html")
