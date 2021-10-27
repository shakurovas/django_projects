from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'announcement', 'text', 'date']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Title'
            }),
            'announcement': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Announcement'
            }),
            'text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Text of the article'
            }),
            'date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Date of publication'
            }),
        }
