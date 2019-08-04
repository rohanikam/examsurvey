from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm


class CustomUserCreateForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = get_user_model()
        fields = "email",


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = get_user_model()
        fields = "email",


class RegisterForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = get_user_model()
        fields = "email", "first_name", "last_name","username",

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.fields["first_name"].required = True

from django import forms
from users.models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserUpdateForm(forms.ModelForm):
        email = forms.EmailField()
        class Meta:
            model = CustomUser
            fields = ['first_name','last_name','email','username']
class ProfileUpdateForm(forms.ModelForm):
        class Meta:
            model = Profile
            fields = ['image']


            