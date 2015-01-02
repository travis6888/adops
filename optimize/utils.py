from fileinput import filename
from io import BytesIO
from mmap import mmap, ACCESS_READ
import os
import datetime
from wsgiref.util import FileWrapper
import StringIO
import zipfile
from django.conf import settings
from django.http import HttpResponse
import xlrd
# from adops import settings
from xlwt import Workbook
from adops.settings import PROJECT_ROOT, MEDIA_ROOT

__author__ = 'Travis'

def xls_to_response(xls, fname):
    response = HttpResponse(content_type="application/ms-excel")
    response['Content-Disposition'] = 'attachment; filename=%s' % fname
    xls.save(response)
    return response


def handle_uploaded_file(f, name_file):
    with open(settings.MEDIA_ROOT + '{}.xls'.format(name_file), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def check_cell_type(num, row_types, row_value):
    if row_types[num] == 5:
        return int(0)
    else:
        return row_value[num]


# def download():
#
#     date = datetime.datetime.now()
#     new_xl_file = 'Ad_optimization_%s_%s_%s'% (date.day, date.month, date.year)+'.xls'
#     xls2 = (os.path.join(MEDIA_ROOT, new_xl_file))
#     with open(xls2, 'rb') as f:
#         workbook = xlrd.open_workbook(xls2)
#         print workbook
#
#         response = HttpResponse(f, content_type='application/vnd.ms-excel')
#         response['Content-Disposition'] = 'attachment; filename='+new_xl_file
#         return response

def create_excel(row_val, curr_row, num_rows, text, ws, wb, row_types):
    ws.row(curr_row).write(0, u'{}'.format(text))
    ws.row(curr_row).write(1, check_cell_type(0, row_types, row_val))
    ws.row(curr_row).write(2, check_cell_type(1, row_types, row_val))
    ws.row(curr_row).write(3, check_cell_type(2, row_types, row_val))
    ws.row(curr_row).write(4, check_cell_type(3, row_types, row_val))
    ws.row(curr_row).write(5, check_cell_type(4, row_types, row_val))
    ws.row(curr_row).write(6, check_cell_type(5, row_types, row_val))
    ws.row(curr_row).write(7, check_cell_type(6, row_types, row_val))
    ws.row(curr_row).write(8, check_cell_type(7, row_types, row_val))
    ws.row(curr_row).write(9, check_cell_type(8, row_types, row_val))
    ws.row(curr_row).write(10, check_cell_type(9, row_types, row_val))
    ws.row(curr_row).write(11, check_cell_type(10, row_types, row_val))
    ws.row(curr_row).write(12, check_cell_type(11, row_types, row_val))
    ws.row(curr_row).write(13, check_cell_type(12, row_types, row_val))
    ws.row(curr_row).write(14, check_cell_type(13, row_types, row_val))
    ws.row(curr_row).write(15, check_cell_type(14, row_types, row_val))
    ws.row(curr_row).write(16, check_cell_type(15, row_types, row_val))
    ws.row(curr_row).write(17, check_cell_type(16, row_types, row_val))
    ws.row(curr_row).write(18, check_cell_type(17, row_types, row_val))
    ws.row(curr_row).write(19, check_cell_type(18, row_types, row_val))
    ws.row(curr_row).write(20, check_cell_type(19, row_types, row_val))
    ws.row(curr_row).write(21, check_cell_type(20, row_types, row_val))
    ws.row(curr_row).write(22, check_cell_type(21, row_types, row_val))
    ws.row(curr_row).write(23, check_cell_type(22, row_types, row_val))
    ws.row(curr_row).write(24, check_cell_type(23, row_types, row_val))
    # # rows +=1
    return


def open_file_sort(buffer, sheet, impressions, clicks, name, clicks_loc, imp_loc, ctr, ctr_loc, su_imp, su_imp_loc, su, su_loc):
    file_dir = (os.path.join(PROJECT_ROOT, "static", name))
    with open(file_dir, 'rb') as f:
        workbook = xlrd.open_workbook(file_dir)
        sheet_num = (sheet - 1)
        worksheet = workbook.sheet_by_index(sheet_num)
        num_rows = worksheet.nrows - 1
        wb = Workbook()
        ws = wb.add_sheet('Ad optimization', cell_overwrite_ok=True)
        curr_row = 0
        curr_rows = 0
        # data = []
        while curr_row < num_rows:
            row = worksheet.row(curr_row)
            row_val = worksheet.row_values(curr_row, 0, None)
            row_types = worksheet.row_types(curr_row, 0, None)
            # need to add su_imp error check
            if row_types[su_loc] == 5:
                if row_val[imp_loc] >= impressions and row_val[clicks_loc] >= clicks:
                    text = "no signups, impressions more than " + str(impressions) + " and clicks GT " + str(clicks)
                    create_excel(row_val, curr_row, num_rows, text, ws, wb, row_types)
                elif row_val[imp_loc] >= impressions:
                    text = "no signups, impressions more than " + str(impressions)
                    create_excel(row_val, curr_row, num_rows, text, ws, wb, row_types)
                elif row_val[clicks_loc] >= clicks:
                    text = "no signups, clicks GT " + str(clicks)
                    create_excel(row_val, curr_row, num_rows, text, ws, wb, row_types)
                else:
                    text = "not enough impressions or clicks "
                    create_excel(row_val, curr_row, num_rows, text, ws, wb, row_types)
            else:
                if row_val[su_loc] >= su:

                    if row_val[su_imp_loc] >= su_imp and row_val[ctr_loc] >= ctr and row_types[su_imp_loc] != 5:
                        text = "ad is performing"
                        create_excel(row_val, curr_row, num_rows, text, ws, wb, row_types)
                    elif row_val[su_imp_loc] < su_imp and row_val[ctr_loc] >= ctr and row_types[su_imp_loc] != 5:
                        text = "ad has underperforming SU/Imp rate but performing CTR "
                        create_excel(row_val, curr_row, num_rows, text, ws, wb, row_types)
                    elif row_val[su_imp_loc] >= su_imp and row_val[ctr_loc] < ctr and row_types[su_imp_loc] != 5:
                        text = "ad has underperforming CTR but performing SU/Imp rate "
                        create_excel(row_val, curr_row, num_rows, text, ws, wb, row_types)
                    elif row_val[su_imp_loc] <= su_imp and row_val[ctr_loc] <= ctr and row_types[su_imp_loc] != 5:
                        text = "ad is underperforming"
                        create_excel(row_val, curr_row, num_rows, text, ws, wb, row_types)
                    elif row_types[su_imp_loc] == 5:
                        text = "no su's"
                        create_excel(row_val, curr_row, num_rows, text, ws, wb, row_types)
                    else:
                        print "error, su's missed something" + str(curr_row)
                        text = "check error"
                        create_excel(row_val, curr_row, num_rows, text, ws, wb, row_types)
                else:
                    if row_val[su_imp_loc] >= su_imp and row_val[ctr_loc] >= ctr and row_types[su_imp_loc] != 5:
                        text = "ad is performing but SU's are less than " + str(su)
                        create_excel(row_val, curr_row, num_rows, text, ws, wb, row_types)
                    elif row_val[su_imp_loc] < su_imp and row_val[ctr_loc] >= ctr and row_types[su_imp_loc] != 5:
                        text = "ad has underperforming SU/Imp rate but performing CTR and SU's are less than " + str(su)
                        create_excel(row_val, curr_row, num_rows, text, ws, wb, row_types)
                    elif row_val[su_imp_loc] >= su_imp and row_val[ctr_loc] < ctr and row_types[su_imp_loc] != 5:
                        text = "ad has underperforming CTR but performing SU/Imp rate and SU's are less than " + str(su)
                        create_excel(row_val, curr_row, num_rows, text, ws, wb, row_types)
                    elif row_val[su_imp_loc] <= su_imp and row_val[ctr_loc] <= ctr and row_types[su_imp_loc] != 5:
                        text = "ad is underperforming"
                        create_excel(row_val, curr_row, num_rows, text, ws, wb, row_types)
                    elif row_types[su_imp_loc] == 5:
                        text = "no su's"
                        create_excel(row_val, curr_row, num_rows, text, ws, wb, row_types)
                    else:
                        print "error, su's missed something" + str(curr_row)
                        text = "check error"
                        create_excel(row_val, curr_row, num_rows, text, ws, wb, row_types)

                    text = "not enough signups"
                    create_excel(row_val, curr_row, num_rows, text, ws, wb, row_types)
            curr_row += 1

        date = datetime.datetime.now()
        new_xl_file = 'Ad_optimization_%s_%s_%s'% (date.day, date.month, date.year)+'.xls'
        xls2 = wb.save(os.path.join(MEDIA_ROOT, new_xl_file))
        download()

        return
        # xls_to_response(xls, new_xl_file)

