from django import forms
from blog.models import Comment_blog


class Comment_detail_Form(forms.ModelForm):
    class Meta:
        model = Comment_blog
        fields = ( 'name', 'surname', 'phone',  'comment',)