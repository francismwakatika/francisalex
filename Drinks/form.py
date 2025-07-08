from django import forms
from .models import Customer
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'locality', 'country', 'mobile', 'zipcode', 'city']

    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Full Name',
    }))

    locality = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Locality',
    }))
    
    country = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Country',
    }))

    mobile = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'placeholder': 'Mobile Number',
    }))

    zipcode = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'placeholder': 'Zipcode',
    }))

    city = forms.ChoiceField(choices=Customer.STATE_CHOICE, widget=forms.Select(attrs={
        'class': 'form-select',
    }))


class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Old Password'
        })
    )
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'New Password'
        })
    )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirm New Password'
        })
    )

    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']


class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your email'
        }),
        label='Email',
    )
