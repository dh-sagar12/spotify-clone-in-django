# from django import forms
from .models import User
from django.contrib.auth import forms, password_validation 
from django import forms as f
from django.utils.translation import gettext_lazy as _

class UserChangeForm(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model = User


class UserCreationForm(forms.UserCreationForm):
    
    
    
    def __init__(self, *args, **kwargs):
            super(UserCreationForm, self).__init__(*args, **kwargs)
            for visible in self.visible_fields():
                visible.field.widget.attrs['class'] = 'form-control rounded-left'
    
    password1 = f.CharField(
        label=_("Password"),
        strip=False,
        widget=f.PasswordInput(attrs={'autocomplete': 'new-password', 'placeholder': 'Choose your password'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = f.CharField(
        label=_("Password confirmation"),
        widget=f.PasswordInput(attrs={'autocomplete': 'new-password', 'placeholder': 'Confirm your password'}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )

    class Meta:
        model = User
        fields = ("username", "email","first_name", "last_name", "date_of_birth", 'gender')
        widgets= {
            'username': f.TextInput(attrs={'placeholder': 'Choose an username', 'autofocus': True}),
            'email': f.EmailInput(attrs= {'placeholder': 'Enter your valid email address', }),
            'first_name': f.TextInput(attrs= {'placeholder': 'First Name'}),
            'last_name': f.TextInput(attrs= {'placeholder': 'Last Name'}),
            'date_of_birth': f.DateTimeInput(attrs= {'placeholder': 'Date of Birth', 'type': 'date'}),
            'password1': f.PasswordInput(attrs={'placeholder': 'Choose a password'}),
            'password2': f.PasswordInput(attrs={'placeholder': 'Confirm your password'}),
            'gender': f.Select(attrs={'placeholder':'Select yout gender',})
        }
        