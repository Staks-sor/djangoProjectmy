from django import forms
from .models import Category


class NewsForm(forms.Form):
    title = forms.CharField(max_length=150)
    content = forms.CharField()
    # photo = forms.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True)
    is_published = forms.BooleanField()
    category = forms.ModelChoiceField(queryset=Category.objects.all())