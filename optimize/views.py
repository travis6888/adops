import csv
from mmap import mmap, ACCESS_READ
from sys import path
from django.shortcuts import render

# Create your views here.
from pandas import ExcelFile, pandas
import xlrd


def home(request):
    # print df
    with open('optimize/adopstest.xls','rb') as f:
        print xlrd.open_workbook(file_contents=mmap(f.fileno(),0,access=ACCESS_READ))
        aString = open('optimize/adopstest.xls','rb').read()
        workbook = xlrd.open_workbook('optimize/adopstest.xls')
            # xlrd.open_workbook(file_contents=aString)
        worksheet = workbook.sheet_by_name('Sheet1')
        num_rows = worksheet.nrows-1
        curr_row = -1
        while curr_row < num_rows:
            row = worksheet.row(curr_row)
            row_val = worksheet.row_values(curr_row, 0,None)
            # print row_val[9]
            if row_val[10] > 0:
                print "impressions", row_val[10]
                if row_val[9] > 0:
                    print "yes clicks and impressions"
                else:
                    print " impressions and no clicks"

            else:
                print "no"
            curr_row += 1

    return render(request, 'home.html')