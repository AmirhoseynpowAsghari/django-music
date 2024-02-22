from django import forms
from django.forms import ModelForm
from .models import Music

class MusicForm(ModelForm):
    # Define choices for the category field
    CATEGORY_CHOICES = [
        ('rock', 'Rock'),
        ('pop', 'Pop'),
        ('classic', 'Classic'),
        ('jazz', 'Jazz'),
        ('hip-hop', 'Hip Hop'),
        ('pop-rock', 'Pop Rock'),
        ('metal', 'Metal'),
        ('hard-rock', 'Hard Rock'),
        ('persian-pop', 'Persian Pop'),
        ('persian-rock', 'Persian Rock'),
    ]
    
    # Define the category field with the predefined choices
    category = forms.ChoiceField(choices=CATEGORY_CHOICES, label='Category', widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Music
        fields = ['name', 'category', 'description']
        labels = {
            'name': 'Music Name',
            'description': 'Description',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Music Name'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description'}),
        }
