from django import forms
from .models import Post

class InputForm(forms.Form):
    model = Post
    fields = ['People', 'Address', 'Doctor', 'Product', 'Bio']
