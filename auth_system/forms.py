from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from .models import CustomUser


class CustomPasswordWidget(forms.PasswordInput):
    def render(self, name, value, attrs=None, renderer=None):
        input_html = super().render(name, value, attrs, renderer)

        return mark_safe(
            f'{input_html} <p>Hello</p>'
        )


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2']

    def init(self, args, **kwargs):
        super().init(args, **kwargs)

        self.fields['password1'].widget = CustomPasswordWidget(attrs={
            'class': 'password-input',
            'placeholder': 'Enter your password',
            "required": True,
        })

        self.fields['password2'].widget = CustomPasswordWidget(attrs={
            'class': 'password-input',
            'placeholder': 'Enter your password',
            "required": True,
        })