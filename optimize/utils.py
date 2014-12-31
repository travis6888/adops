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


def check_cell_type(num, row_types, row_value):
    if row_types[num] == 5:
        print num
        return int(0)
    else:
        return row_value[num]


def create_excel(row_val, curr_row, num_rows, worksheet, ws, wb, row_types):
    ws.row(curr_row).write(0, u'{}'.format("text"))
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


def open_file_sort(sheet, impressions, clicks, name, clicks_loc, imp_loc, ctr, ctr_loc, su_imp, su_imp_loc, su, su_loc):
    file_dir = (os.path.join(PROJECT_ROOT, "static", name))
    with open(file_dir, 'rb') as f:
        workbook = xlrd.open_workbook(file_dir)
        sheet_num = (sheet - 1)
        worksheet = workbook.sheet_by_index(sheet_num)
        num_rows = worksheet.nrows - 1
        wb = Workbook()
        ws = wb.add_sheet('Type examples', cell_overwrite_ok=True)
        curr_row = 0
        curr_rows = 0
        # data = []
        while curr_row < num_rows:
            row = worksheet.row(curr_row)
            row_val = worksheet.row_values(curr_row, 0, None)
            row_types = worksheet.row_types(curr_row, 0, None)
            # data.append(row_val)
            # print row_val[9]
            if row_val[imp_loc] > impressions:
                print "impressions", row_val[10], curr_row
                if row_val[clicks_loc] > clicks:
                    create_excel(row_val, curr_row, num_rows, worksheet, ws, wb, row_types)

                    # print "yes clicks and impressions"
                    if row_types[su] == 5:
                        create_excel(row_val, curr_row, num_rows, worksheet, ws, wb, row_types)
                        # print "click, impressions but no su"
                    elif row_val[su_loc] > su:
                        create_excel(row_val, curr_row, num_rows, worksheet, ws, wb, row_types)

                        # print "clicks impressions and signups greater than " + str(su)
                    else:
                        create_excel(row_val, curr_row, num_rows, worksheet, ws, wb, row_types)

                        # print "su's {}".format(row_val[16]), row_val[10], curr_row
                else:
                    create_excel(row_val, curr_row, num_rows, worksheet, ws, wb, row_types)
                    #
                    # # print " impressions and no clicks"
            else:
                if row_types[su_loc] == 5:
                    create_excel(row_val, curr_row, num_rows, worksheet, ws, wb, row_types)

                    # print "this is error"
                else:
                    create_excel(row_val, curr_row, num_rows, worksheet, ws, wb, row_types)
                    # print row_val[su_loc]
            curr_row += 1
            wb.save('types.xls')