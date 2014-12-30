from fileinput import filename
from mmap import mmap, ACCESS_READ
import os
from django.conf import settings
import xlrd
# from adops import settings
from xlwt import Workbook
from adops.settings import PROJECT_ROOT

__author__ = 'Travis'


def xls_proc_text(cell, value_proc=None, text_proc=None):
    """Converts the given cell to appropriate text."""
    """The proc will come in only when the given is value or text."""
    ttype = cell.ctype
    if ttype == xlrd.XL_CELL_EMPTY or ttype == xlrd.XL_CELL_TEXT or ttype == xlrd.XL_CELL_BLANK:
        if text_proc is None:
            return cell.value
        else:
            return text_proc(cell.value)
    if ttype == xlrd.XL_CELL_NUMBER or ttype == xlrd.XL_CELL_DATE or ttype == xlrd.XL_CELL_BOOLEAN:
        if value_proc is None:
            return str(cell.value)
        else:
            return str(value_proc(cell.value))
    if cell.ctype == xlrd.XL_CELL_ERROR:
        # Apply no proc on this.
        return xlrd.error_text_from_code[cell.value]


def handle_uploaded_file(f, name_file):

    with open(settings.MEDIA_ROOT + '{}.xls'.format(name_file), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def create_excel(row_val, curr_rows, num_rows):
    wb = Workbook()
    ws = wb.add_sheet('Type examples')
    rows = 0
    # for x in data:
    while rows < num_rows:
        ws.row(rows).write(0,u'{}'.format("text"))
    # ws.row(0).write(1, row_val[0])
    # ws.row(0).write(2, row_val[1])
    # ws.row(0).write(3, row_val[3])
    # ws.row(0).write(4, row_val[4])
    # ws.row(0).write(5, row_val[5])
    # ws.row(0).write(6, row_val[6])
        rows +=1

    wb.save('types.xls')


def open_file_sort(sheet, impressions, clicks, name, clicks_loc, imp_loc, ctr, ctr_loc, su_imp, su_imp_loc, su, su_loc):
    file_dir = (os.path.join(PROJECT_ROOT, "static", name))
    with open(file_dir,'rb') as f:
        workbook = xlrd.open_workbook(file_dir)
        sheet_num = (sheet - 1)
        worksheet = workbook.sheet_by_index(sheet_num)
        num_rows = worksheet.nrows-1
        curr_row = -1
        curr_rows = 0

        while curr_row < num_rows:
            row = worksheet.row(curr_row)
            row_val = worksheet.row_values(curr_row, 0, None)
            row_types = worksheet.row_types(curr_row, 0, None)
            # print row_val[9]
            if row_val[imp_loc] > impressions:
                print "impressions", row_val[10], curr_row
                if row_val[clicks_loc] > clicks:
                    create_excel(row_val, curr_rows, num_rows)

                    print "yes clicks and impressions"
                    if row_types[su] == 5:
                        create_excel(row_val, curr_rows, num_rows)
                        print "click, impressions but no su"
                    elif row_val[su_loc] > su:
                        create_excel(row_val, curr_rows, num_rows)

                        print "clicks impressions and signups greater than " + str(su)
                    else:
                        create_excel(row_val, curr_rows, num_rows)

                        print "su's {}".format(row_val[16]), row_val[10], curr_row
                else:
                    create_excel(row_val, curr_rows, num_rows)

                    print " impressions and no clicks"
            else:
                if row_types[su_loc] == 5:
                    # create_excel(row_val, curr_rows)

                    print "this is error"
                else:
                    create_excel(row_val, curr_rows, num_rows)

                    print row_val[su_loc]
            curr_row += 1
            curr_rows += 1