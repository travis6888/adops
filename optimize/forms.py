from django import forms
from django.forms import TextInput

__author__ = 'Travis'


class FileForm(forms.Form):
    name = forms.CharField(max_length=12, required=True, widget=forms.TextInput({ "placeholder": "File Name"}))
    file = forms.FileField()
    sheet_num = forms.IntegerField(widget=forms.TextInput({ "placeholder": "Sheet Number"}))
    ctr = forms.DecimalField(widget=forms.TextInput({ "placeholder": "Click Thru Rate"}))
    ctr_loc = forms.IntegerField(widget=forms.TextInput({ "placeholder": "Column location of CTR"}))
    click = forms.IntegerField(widget=forms.TextInput({ "placeholder": "Lowest # of clicks"}))
    click_loc = forms.IntegerField(widget=forms.TextInput({ "placeholder": "Column location of Clicks"}))
    su_to_imp = forms.DecimalField(widget=forms.TextInput({ "placeholder": "Lowest SU/IMP percentage"}))
    su_to_imp_loc = forms.IntegerField(widget=forms.TextInput({ "placeholder": "Column location of SU/IMP"}))
    impressions = forms.IntegerField(widget=forms.TextInput({ "placeholder": "Lowest number of Impressions"}))
    imp_loc = forms.IntegerField(widget=forms.TextInput({ "placeholder": "Column location of Impressions"}))
    su = forms.IntegerField(widget=forms.TextInput({ "placeholder": "Lowest Number of SU's"}))
    su_loc = forms.IntegerField(widget=forms.TextInput({ "placeholder": "Column Location of SU's"}))
