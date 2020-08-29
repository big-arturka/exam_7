from django import forms
from .models import Poll, Choice


class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ['question']
        widgets = {'question': forms.TextInput(attrs={'class': 'form-input'}),
                   }


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['variant']
        widgets = {'variant': forms.TextInput(attrs={'class': 'form-input'}),
                   }