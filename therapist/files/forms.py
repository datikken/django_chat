from django import forms

class DocumentFrom(forms.Form):
    document = forms.FileField()