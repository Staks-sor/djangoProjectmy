from django import forms
from .models import News
# from .models import Category


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



    # title = forms.CharField(max_length=150, label='Название новости', widget=forms.TextInput(attrs={"class": "form-control"}))
    # content = forms.CharField(label='Содержание', required=False, widget=forms.Textarea(attrs={"class": "form-control", "rows": 5}))
    # # photo = forms.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True)
    # is_published = forms.BooleanField(label='Публикация', initial=True)
    # category = forms.ModelChoiceField(empty_label='Выбор категории', queryset=Category.objects.all(), label='Категория', widget=forms.Select(attrs={"class": "form-control"}))
