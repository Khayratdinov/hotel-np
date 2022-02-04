from django import forms
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput, FileInput, NumberInput, DateInput
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from accounts.models import CustomUser


# ─────────────────────────────── USER REGISTER ────────────────────────────── #


class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'full_name', 'email', 'phone', 'password1', 'password2', )

        widgets = {
            "username": TextInput(attrs={
                'class': 'form-control',
                'id': 'name',
                'placeholder': 'Enter your name'
            }),
            "full_name": TextInput(attrs={
                'class': 'form-control',
                'id': 'fullname',
                'placeholder': 'Enter your name'
            }),
            "email": EmailInput(attrs={
                'class': 'form-control',
                'id': 'emailaddress',
                'placeholder': 'Enter your email'
            }),
            "phone": TextInput(attrs={
                'class': 'form-control',
                'id': 'phone',
                'placeholder': 'Enter your phone'
            }),

            "password1": PasswordInput(attrs={
                'class': 'form-control',
                'id': 'password1',
                'placeholder': 'Enter your password'
            }),
            "password2": PasswordInput(attrs={
                'class': 'form-control',
                'id': 'password2',
                'placeholder': 'Enter your password'
            }),
        }


class UserUpdateForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'full_name', 'email', 'phone', 'birthday',
                  'avatar',  'address', 'city', 'country', 'zip', 'bio')
