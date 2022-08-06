from django import forms

class Boardform(forms.Form):
    title = forms.CharField(
        max_length=64,
        label='제목'
    )
    contents = forms.CharField(
        widget=forms.Textarea, label='내용')
