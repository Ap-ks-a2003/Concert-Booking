# forms.py
from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['username', 'email', 'contact_no', 'num_of_people']
        # Add other fields as needed
