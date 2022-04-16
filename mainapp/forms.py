from django import forms
from django.forms import widgets, CheckboxInput
from django.utils.html import conditional_escape, escape
from django.utils.safestring import mark_safe

from .models import *
from django.forms import ClearableFileInput


class CustomClearableFileInput(ClearableFileInput):
    template_name = 'widgets/file_input.html'


class AdForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = [
            'services', 'name', 'description', 'price', 'city', 'services', 'image'
        ]
        widgets = {
            'services': forms.CheckboxSelectMultiple,
            'image': CustomClearableFileInput
        }

    def __init__(self, *args, **kwargs):
        super(AdForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'class': 'form-control'})
        self.fields['price'].widget.attrs.update({'class': 'form-control'})
        self.fields['city'].widget.attrs.update({'class': 'form-control'})
        self.fields['image'].widget.attrs.update({'class': 'form-control'})
