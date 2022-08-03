import re
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class ResetPassword(forms.Form):
    new_password = forms.CharField()  # TODO: add length of password
    confirm_new_password = forms.CharField()

    def clean(self):
        new_password = self.cleaned_data['new_password'] #
        if len(new_password) < 8:
            raise ValidationError(_('Password must be at least 8 characters'))
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






