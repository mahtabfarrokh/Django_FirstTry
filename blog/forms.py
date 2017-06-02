# In The Name Of God 
# Creation Date : 3/19/17
# Created By : Mahtab Farrokh (mahtab.farrokh@gmail.com)

from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)