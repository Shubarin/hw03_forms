from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('group', 'text')
        help_texts = {
            'group': 'Сообщество для публикации',
            'text': 'Текст сообщения (поста)'
        }
        labels = {'group': 'Сообщество',
                  'text': 'Текст сообщения'}
