from django import forms

__author__ = 'Travis'


class FileForm(forms.Form):
    file = forms.FileField()
