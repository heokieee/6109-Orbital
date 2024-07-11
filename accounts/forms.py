
# accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Reminder

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    username = forms.CharField(max_length=150, required=True)  # Define username field separately

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.username = self.cleaned_data['username']  # Assign username from form input

        if commit:
            user.save()
        
        return user
    

class ReminderForm(forms.ModelForm):
    class Meta:
        model = Reminder
        fields = ['title', 'description', 'date', 'time', 'priority']
