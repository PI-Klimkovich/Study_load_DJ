from django import forms
from user.models import User


class RegisterForm(forms.Form):
    username = forms.CharField(min_length=3, max_length=50)
    email = forms.EmailField(max_length=50)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    last_name = forms.CharField(min_length=3, max_length=50)
    first_name = forms.CharField(min_length=3, max_length=50)

    # Методы для валидации полей называются: `clean_` + `название поля`
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username and User.objects.filter(username=username).exists():
            raise forms.ValidationError('Пользователь с таким username уже существует')
        return self.cleaned_data['username']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and User.objects.filter(email=email).exists():
            raise forms.ValidationError('Пользователь с таким email уже существует')
        return self.cleaned_data['email']

    # Общая проверка после проверки всех полей.
    def clean(self):
        data = self.cleaned_data
        if data["password1"] != data["password2"]:
            raise forms.ValidationError("Пароли не совпадают!")
        return data
