from django import forms

from .widgets import AjaxInputWidget
from .models import City


class SearchTicket(forms.Form):
    departure_city = forms.CharField(label='Город отправления', widget=AjaxInputWidget)
    arrival_city = forms.ModelChoiceField(queryset=City.objects.all(), label='Город прибытия')
