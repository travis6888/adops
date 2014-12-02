import csv
from django.shortcuts import render

# Create your views here.


def home(request):
    # with open(path) as f:
    #     reader = csv.reader(f)
    #     for row in reader:
    return render(request, 'home.html')