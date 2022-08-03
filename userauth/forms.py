import re
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class ResetPassword(forms.Form): 

    new_password = forms.CharField(min_length=8, widget=forms.PasswordInput(attrs={'id':'new_password', 'type':'password', 'placeholder':'Enter new password'}))  # TODO: add length of password
    confirm_new_password = forms.CharField(min_length=8, widget=forms.PasswordInput(attrs={'id':'confirm_new_password', 'type':'password', 'placeholder':'Confirm new password'}))  # TODO: add length of password

    def clean(self):
<<<<<<< HEAD
        new_password = self.cleaned_data['new_password'] #
        if len(new_password) < 8:
            raise ValidationError(_('Password must be at least 8 characters'))
||||||| b4f0e7e
        new_password = self.cleaned_data['new_password']
        if len(new_password) < 8:
            raise ValidationError(_('Password must be at least 8 characters'))
=======
        new_password = self.cleaned_data['new_password']

>>>>>>> 85b93c6d051b8c19e01b0b2dc93af5126232d456
        if not bool(re.search(r'\d', new_password)):
            raise ValidationError(
                _('Password must contain at least one digit'))

        confirm_new_password = self.cleaned_data['confirm_new_password']

        if confirm_new_password != new_password:
            raise ValidationError(_('Passwords do not match'))

        return self.cleaned_data


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email","password1","password2")


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1")






