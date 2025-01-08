from django import forms
from .models import Person

class PersonalPageForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['full_name', 'bio', 'photo', 'resume']