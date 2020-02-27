from django.forms import ModelForm, TextInput
from .models import Movie

class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ['title']
        widgets = {'title': TextInput(attrs={'class':'form-control', 'placeholder':'Enter movie title'})}