from django import forms
from .models import Comment


class Contact(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=100 )
    email_address = forms.EmailField(max_length=150)
    message = forms.CharField(max_length=1000000, widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
