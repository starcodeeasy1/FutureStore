#REGISTRATION FORM
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
class RegistrationForm(UserCreationForm):
    password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
    class Meta:
        model=User
        fields=["first_name",
                "last_name",
                "email",
                "username",
                "password1",
                "password2"]
        widgets={
            "first_name":forms.TextInput(attrs={"class":"form-control"}),
            "last_name":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"}),
            "username":forms.TextInput(attrs={"class":"form-control"})
            }
#LOGIN FORM
class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
#CART FORM
class CartForm(forms.Form):
    quantity=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}))
#ORDER FORM
class OrderForm(forms.Form):
    delivery_address=forms.CharField(widget=forms.Textarea(attrs={"class":"form-control"}))
