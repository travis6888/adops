from fileinput import filename
from mmap import mmap, ACCESS_READ
from django.conf import settings
import xlrd
# from adops import settings

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


def open_file_sort():
    with open('optimize/adopstest.xls','rb') as f:
        print xlrd.open_workbook(file_contents=mmap(f.fileno(),0,access=ACCESS_READ))
        aString = open('optimize/adopstest.xls','rb').read()
        workbook = xlrd.open_workbook('optimize/adopstest.xls')
            # xlrd.open_workbook(file_contents=aString)
        worksheet = workbook.sheet_by_index(0)
        num_rows = worksheet.nrows-1
        curr_row = -1
        while curr_row < num_rows:
            row = worksheet.row(curr_row)
            row_val = worksheet.row_values(curr_row, 0,None)
            row_types = worksheet.row_types(curr_row, 0, None)
            # print row_val[9]
            if row_val[10] > 0:
                print "impressions", row_val[10], curr_row
                if row_val[9] > 0:
                    print "yes clicks and impressions"
                    if row_types[16] == 5:
                        print "click, impressions but no su"
                    else:
                        print "su's {}".format(row_val[16]), row_val[10], curr_row
                else:

                        print " impressions and no clicks"
            else:
                if row_types[16] == 5:
                    print "this is error"
                else:
                    print row_val[16]
            curr_row += 1