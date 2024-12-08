# django.contrib.auth.forms => UserCreationForm => it provides fields "password1","password2" and validation etc

from django import forms

from store.models import User,Order

from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):

    class Meta:

        model=User

        fields=["username","email","password1","password2","phone"]

class LoginForm(forms.Form):

    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control mb-3"}))

    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control mb-3"}))


class OrderForm(forms.ModelForm):

    class Meta:

        model=Order

        fields=["address","phone","payment_method"]
