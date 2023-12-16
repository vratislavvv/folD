from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(widget=forms.PasswordInput(), label="Password")

class RegisterForm(forms.Form):
    create_username = forms.CharField(label="Create username")
    create_password = forms.CharField(widget=forms.PasswordInput(), label="Create password")
    repeat_password = forms.CharField(widget=forms.PasswordInput(), label="Repeat password")