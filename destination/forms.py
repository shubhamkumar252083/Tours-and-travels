from django import forms


class BookingForm(forms.Form):

    name = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={

            'name': 'name',
            'placeholder': 'enter your name',
            'class': "inputBox"
        }
    ))
    email = forms.EmailField(widget=forms.TextInput(
        attrs={
            'name': 'email',
            'placeholder': 'enter your email'
        }
    ))
    phone = forms.IntegerField(widget=forms.NumberInput(
        attrs={
            'name': 'phone',
            'placeholder': 'enter your number',
            'class': "inputBox"
        }
    ))

    address = forms.CharField(max_length=200, widget=forms.TextInput(
        attrs={
            'name': 'address',
            'placeholder': 'enter your address',
            'class': "inputBox"
        }
    ))
    location = forms.CharField(max_length=200, widget=forms.TextInput(
        attrs={
            'name': 'location',
            'placeholder': 'place you want to visit',
            'class': "inputBox"
        }
    ))
    guests = forms.IntegerField(widget=forms.NumberInput(
        attrs={
            'name': 'guests',
            'placeholder': 'number of guests',
            'class': "inputBox"
        }
    ))
    arrivals = forms.DateField(widget=forms.NumberInput(
        attrs={
            'name': 'arrivals',
            'type': 'date',
            'class': "inputBox"

        }
    ))
    leaving = forms.DateField(widget=forms.NumberInput(
        attrs={
            'name': 'leaving',
            'type': 'date',
            'class': "inputBox"
        }
    ))
