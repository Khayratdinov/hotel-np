from django import forms
from blog.models import Comment_blog
from django.forms import NumberInput, TextInput, EmailInput, Textarea


class CommentBlogForm(forms.ModelForm):

    class Meta:
        model = Comment_blog
        fields = ['name', 'phone', 'email', 'comment']

        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'id': 'name',
                'placeholder': 'name'
            }),

            "phone": NumberInput(attrs={
                'class': 'form-control',
                'id': 'phone',
                'placeholder': 'phone'
            }),


            "email": EmailInput(attrs={
                'class': 'form-control',
                'id': 'email',
                'placeholder': 'email'
            }),

            "comment": Textarea(attrs={
                'class': 'form-control',
                'id': 'comment',
                'placeholder': 'comment'
            }),



        }
