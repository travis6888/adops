import datetime
import os


from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from adops.settings import MEDIA_ROOT
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
            clicks_loc = form.cleaned_data['click_loc']
            imp_loc = form.cleaned_data['imp_loc']
            ctr = form.cleaned_data['ctr']
            ctr_loc = form.cleaned_data['ctr_loc']
            su_imp = form.cleaned_data['su_to_imp']
            su_imp_loc = form.cleaned_data['su_to_imp_loc']
            su = form.cleaned_data['su']
            su_loc = form.cleaned_data['su_loc']
            name = "media{}{}".format(form.cleaned_data['name'], ".xls")
            open_file_sort(sheet, impressions, clicks, name, clicks_loc, imp_loc, ctr, ctr_loc, su_imp, su_imp_loc, su,
                           su_loc)
            return HttpResponseRedirect('/download/')
    else:
        form = FileForm
    return render(request, 'upload.html', {'form': form})


def download(request):
    date = datetime.datetime.now()
    new_xl_file = 'Ad_optimization_%s_%s_%s' % (date.day, date.month, date.year)+'.xls'
    xls2 = (os.path.join(MEDIA_ROOT, new_xl_file))
    with open(xls2, 'rb') as f:
        response = HttpResponse(f, content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename='+new_xl_file
        return response