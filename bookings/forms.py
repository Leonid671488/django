from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from bookings.models import Booking, Feedback
from django import forms

class BookingForm(forms.ModelForm):
    time = forms.DateTimeField(widget=forms.DateTimeInput(attrs={
        "class": "form-group-input"
    }))
    peoples = forms.IntegerField(widget=forms.NumberInput(attrs={
        "class": "form-group-input",
        "value": "1"
    }))
    pre_order = forms.CharField(widget=forms.Textarea(attrs={
        "class": "form-group-textarea",
        "placeholder": "Напишите блюда, которые хотели бы заказать"
    }))

    class Meta:
        model = Booking
        fields = ("time", "peoples", "pre_order")


class FeedbackForm(forms.ModelForm):
    mark = forms.IntegerField(widget=forms.NumberInput(attrs={
        "class": "form-group-input",
        "value": "1"
    }))
    text = forms.CharField(widget=forms.Textarea(attrs={
        "class": "form-group-textarea",
        "placeholder": "Напишите блюда, которые хотели бы заказать"
    }))

    class Meta:
        model = Feedback
        fields = ("mark", "text")
