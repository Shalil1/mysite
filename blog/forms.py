from django import forms

class EmailPostForm(forms.Form):
    name = forms.charField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)