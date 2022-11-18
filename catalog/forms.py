from django import forms
from datetime import date
from django.forms import ModelForm
from .models import Book


class AuthorsForm(forms.Form):

    first_name = forms.CharField(label="Имя автора")
    last_name = forms.CharField(label="Фамилия автора")

    date_of_birth = forms.DateField(label="Дата рождения",
                                    widget=forms.widgets.DateInput(format='%m-%d-%Y',attrs={'type':'date'}))
    date_of_death = forms.DateField(label="Дата смерти",
                                    initial=format(date.today()),
                                    widget=forms.widgets.DateInput(attrs={'type':'date'}))


class BookModelForm(ModelForm):
    class Meta:
        model = Book
        fields = {'title', 'genre','language','author','summary','isbn'}
        labels = {'summary': 'Аннтоация'}
        help_texts = {'summary': 'Не более 1000 символов'}

