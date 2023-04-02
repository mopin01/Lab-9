from django import forms
from .models import Place

# Create form to enter new place
class NewPlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ('name', 'visited')