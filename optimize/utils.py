from fileinput import filename
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