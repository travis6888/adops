import csv
from mmap import mmap, ACCESS_READ
from sys import path
from django.shortcuts import render

# Create your views here.
from pandas import ExcelFile, pandas
import xlrd


def home(request):
    # xl = pandas.ExcelFile('optimize/adopstest.xls')
    # # print xl.sheet_names
    #
    # df = xl.parse("Sheet1", )
    # print df
    # df["desired"] = df["10"] == 0
    #     # if x == 0:
    #     #     print "no"
    #     # else:
    #     #     print "yes"
    # print df

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
            row_val = worksheet.row_values(curr_row, 9, 10)
            print row_val[0]
            if row_val[0] > 0:
                print "yes"

            else:
                print "no"

            # print row
            # if row > 0:
            #     print "yes"
            # else:
            #     print "no"
            curr_row += 1
            # print row
            # print worksheet.row(34)

    # f = open('adcoloredreportdjango.csv', 'r')
    # for line in f:
    #     line =  line.split(',')
    #     product = Product()
    # with open(path) as f:
    #     reader = csv.reader(f)
    #     for row in reader:
    #         print row


    return render(request, 'home.html')