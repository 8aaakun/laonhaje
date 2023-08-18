from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class SignUpForm(UserCreationForm):
    profile_picture = forms.ImageField(required=False)  # 필수가 아니므로 required=False로 설정

    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2', 'profile_picture')