from django import forms
from .models import Reviews


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Reviews
        fields = ['review']

    widgets = {
        'review': forms.TextInput(attrs={'class': 'form-control', 'id': 'exampleFormControlTextarea1'}),
    }