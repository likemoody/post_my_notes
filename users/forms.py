from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=30)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(max_length=30)

    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        self.fields['username'].required = False
        self.fields['email'].required = False


    class Meta:
        model = User
        fields = ['username', 'email']
        prefix = 'user-account'


class ProfileUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        self.fields['image'].required = False
        self.fields['description'].required = False

    class Meta:
        model = Profile
        fields = ['image', 'description']
        prefix = 'profile'


