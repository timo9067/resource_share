from django import forms

class PostResourceForm(forms.Form):
    title = forms.CharField() # input with type='text'
    link = forms.URLField() # equal to type='url'
    description = forms.CharField(widget=forms.Textarea) 
