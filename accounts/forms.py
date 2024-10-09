from django import forms
from .models import CustomUser  # Ensure you're using your custom user model
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    ROLE_CHOICES = [
        ('librarian', 'Librarian'),
        ('member', 'Member'),
    ]
    
    # Add the role field
    role = forms.ChoiceField(choices=ROLE_CHOICES, required=True)

    class Meta:
        model = CustomUser  # Ensure this refers to your CustomUser model
        fields = ['username', 'role', 'password1', 'password2']  # Include role in fields

