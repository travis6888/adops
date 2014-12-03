import csv
from mmap import mmap, ACCESS_READ
from sys import path
from django.shortcuts import render

# Create your views here.
import xlrd


def home(request):
    with open('optimize/adopstest.xls','rb') as f:
        print xlrd.open_workbook(file_contents=mmap(f.fileno(),0,access=ACCESS_READ))
        aString = open('optimize/adopstest.xls','rb').read()
        workbook = xlrd.open_workbook('optimize/adopstest.xls')
            # xlrd.open_workbook(file_contents=aString)
        for worksheet in workbook.sheets():
            print worksheet.nrows

    # f = open('adcoloredreportdjango.csv', 'r')
    # for line in f:
    #     line =  line.split(',')
    #     product = Product()
    # with open(path) as f:
    #     reader = csv.reader(f)
    #     for row in reader:
    #         print row


    return render(request, 'home.html')