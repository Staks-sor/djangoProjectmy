from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

import re

# from .models import Category
from .models import News


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя',
                               widget=forms.TextInput(attrs={'class': 'form-control', 'autocomlete': 'off'}))
    password = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя', help_text='Имя не должно содержать оскорбления',
                               widget=forms.TextInput(attrs={'class': 'form-control', 'autocomlete': 'off'}))

    email = forms.EmailField(label='Почта', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль', help_text='Пароль не может быть менее 8 символов',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Подтверждение пароля',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = [
            'title',
            'content',
            'is_published',
            'category'
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }
        # Данный метод вытаскивания приемлем ну не очень практичен
        # fields = '__all__'

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('Название не должно начинаться с цифры')
        return title

    # title = forms.CharField(max_length=150, label='Название новости', widget=forms.TextInput(attrs={"class": "form-control"}))
    # content = forms.CharField(label='Содержание', required=False, widget=forms.Textarea(attrs={"class": "form-control", "rows": 5}))
    # # photo = forms.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True)
    # is_published = forms.BooleanField(label='Публикация', initial=True)
    # category = forms.ModelChoiceField(empty_label='Выбор категории', queryset=Category.objects.all(), label='Категория', widget=forms.Select(attrs={"class": "form-control"}))
