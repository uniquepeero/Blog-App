from django import forms
from django.core.exceptions import ValidationError
from .models import Tag, Post

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['title', 'slug']

        class_name = 'form-control'
        widgets = {
            'title': forms.TextInput(attrs={'class': class_name}),
            'slug': forms.TextInput(attrs={'class': class_name})
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == 'create':
            raise ValidationError('Slug may not be "create"')
        if Tag.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError(f'Slug must be unique. "{new_slug}" already taken')

        return new_slug


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'body', 'tags']

        class_name = 'form-control'
        widgets = {
            'title': forms.TextInput(attrs={'class': class_name}),
            'slug': forms.TextInput(attrs={'class': class_name}),
            'body': forms.Textarea(attrs={'class': class_name}),
            'tags': forms.SelectMultiple(attrs={'class': class_name})
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == 'create':
            raise ValidationError('Slug may not be "create"')

        return new_slug