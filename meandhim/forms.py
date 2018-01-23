from django import forms

class userForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'id': "theFieldID", 'placeholder': 'Type your name...'}),label='')
