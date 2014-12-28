from django import forms

__author__ = 'Travis'


class FileForm(forms.Form):
    name = forms.CharField(max_length=12, required=True)
    file = forms.FileField()
    sheet_num = forms.IntegerField()
