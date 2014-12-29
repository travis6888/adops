from django import forms

__author__ = 'Travis'


class FileForm(forms.Form):
    name = forms.CharField(max_length=12, required=True)
    file = forms.FileField()
    sheet_num = forms.IntegerField()
    ctr = forms.DecimalField()
    ctr_loc = forms.DecimalField()
    click = forms.IntegerField()
    click_loc = forms.DecimalField()
    su_to_imp = forms.DecimalField()
    su_to_imp_loc = forms.DecimalField()
    impressions = forms.IntegerField()
    imp_loc = forms.DecimalField()
    su = forms.IntegerField()
    su_loc = forms.DecimalField()
