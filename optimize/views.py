from StdSuites import cell
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
            row_types = worksheet.row_types(curr_row, 0, None)
            # print row_val[9]
            if row_val[10] > 0:
                print "impressions", row_val[10], curr_row, row_val[16]
                if row_val[9] > 0:
                    print "yes clicks and impressions"
                else:
                    print " impressions and no clicks"


            else:
                if row_types[16] == 5:
                    print "this is error"
                else:
                    print row_val[16]
                # print row_types[16]
                # print cell(curr_row,row_val[16])
                # print "no"
                # print row_val[16]
            curr_row += 1



    return render(request, 'home.html')


