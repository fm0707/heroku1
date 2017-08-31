from django import forms

class DakokuForm(forms.Form):
    text = forms.CharField()
    location = forms.CharField()