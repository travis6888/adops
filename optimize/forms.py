from django import forms

__author__ = 'Travis'


class FileForm(forms.Form):
    name = forms.CharField(max_length=12, required=True)
    file = forms.FileField()
    sheet_num = forms.IntegerField()
    ctr = forms.DecimalField()
    clicks = forms.IntegerField()
    su_to_imp = forms.DecimalField()
    impressions = forms.IntegerField()
    su = forms.IntegerField()
