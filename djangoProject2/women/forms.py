from .models import *
from django import forms


class AddPostForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = 'Категория не выбрана'

    class Meta:
        model = Women
        fields = ['title', 'slug', 'content', 'photo', 'is_published', 'cat']

    # title = forms.CharField(max_length=225, label='Заголовок')
    # slug = forms.SlugField(max_length=225, label='URL')
    # content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}), label='Содержание')
    # is_published = forms.BooleanField(label='Публикация', initial=True)
    # cat = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категория', empty_label='Без категории')
