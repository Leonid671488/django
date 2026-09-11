from bookings.models import Booking, Feedback
from django import forms

class BookingForm(forms.ModelForm):
    time = forms.DateTimeField(widget=forms.DateTimeInput(attrs={
        "type": "datetime-local",
        "class": "form-group-input"
    }))
    peoples = forms.IntegerField(widget=forms.NumberInput(attrs={
        "class": "form-group-input",
        "value": "1",
        "min": "1"
    }))
    pre_order = forms.CharField(widget=forms.Textarea(attrs={
        "class": "form-group-textarea",
        "placeholder": "Напишите блюда, которые хотели бы заказать..."
    }))

    class Meta:
        model = Booking
        fields = ("time", "peoples", "pre_order")


class FeedbackForm(forms.ModelForm):
    mark = forms.IntegerField(widget=forms.NumberInput(attrs={
        "class": "form-group-input",
        "value": "5",
        "min": "1",
        "max": "5"
    }))
    text = forms.CharField(widget=forms.Textarea(attrs={
        "class": "form-group-textarea",
        "placeholder": "Напишите свое мнение о ресторане..."
    }))

    class Meta:
        model = Feedback
        fields = ("mark", "text")
