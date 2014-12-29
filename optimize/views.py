
from django.http import HttpResponseRedirect
from django.shortcuts import render

from optimize.forms import FileForm
from optimize.utils import handle_uploaded_file, open_file_sort


def home(request):

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
            name = "media{}{}".format(form.cleaned_data['name'], ".xls")
            open_file_sort(sheet, impressions, clicks, name)
            return HttpResponseRedirect('/home/')
    else:

        form = FileForm
    return render(request, 'upload.html', {'form': form})


