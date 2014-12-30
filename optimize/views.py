
from django.http import HttpResponseRedirect
from django.shortcuts import render

from optimize.forms import FileForm
from optimize.utils import handle_uploaded_file, open_file_sort, create_excel


def home(request):
    # create_excel()
    return render(request, 'home.html')


def file_upload(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            print "yes"
            handle_uploaded_file(request.FILES['file'], name_file=form.cleaned_data['name'])
            sheet = form.cleaned_data['sheet_num']
            impressions = form.cleaned_data['impressions']
            clicks = form.cleaned_data['click']
            clicks_loc = form.cleaned_data['click_loc']
            imp_loc = form.cleaned_data['imp_loc']
            ctr= form.cleaned_data['ctr']
            ctr_loc = form.cleaned_data['ctr_loc']
            su_imp = form.cleaned_data['su_to_imp']
            su_imp_loc = form.cleaned_data['su_to_imp_loc']
            su = form.cleaned_data['su']
            su_loc = form.cleaned_data['su_loc']


            name = "media{}{}".format(form.cleaned_data['name'], ".xls")
            open_file_sort(sheet, impressions, clicks, name, clicks_loc, imp_loc, ctr, ctr_loc, su_imp, su_imp_loc, su, su_loc)
            return HttpResponseRedirect('/home/')
    else:

        form = FileForm
    return render(request, 'upload.html', {'form': form})


