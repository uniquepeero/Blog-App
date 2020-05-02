from django import forms
from django.core.exceptions import ValidationError
from .models import Tag

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['title', 'slug']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'})
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == 'create':
            raise ValidationError('Slug may not me "create"')
        if Tag.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError(f'Slug must be unique. "{new_slug}" already taken')

        return new_slug
