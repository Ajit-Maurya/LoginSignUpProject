from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)
    profile_picture = forms.ImageField(required=False)
    address_line1 = forms.CharField(max_length=255)
    city = forms.CharField(max_length=255)
    state = forms.CharField(max_length=255)
    pincode = forms.CharField(max_length=10)
    user_type = forms.ChoiceField(choices=CustomUser.USER_TYPE_CHOICES)

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'profile_picture', 'password1', 'password2', 'address_line1', 'city', 'state', 'pincode', 'user_type')
