from django import forms

class DakokuForm(forms.Form):
    text = forms.CharField()