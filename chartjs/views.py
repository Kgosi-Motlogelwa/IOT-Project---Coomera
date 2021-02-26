from django.shortcuts import render
import csv
from .models import Imported_CSVs
# Create your views here.
def index(request):
   
    f = open(r"C:\Users\komot\Google Drive\_Learning Code\Coomera\Coomera_Multiple_Locations_per_sheet.csv") 
    for line in f:
        line =  line.split(',')
        tmp = Imported_CSVs.objects.create()
        tmp.Location = line[0]
        tmp.DateTime = line[1]
        tmp.Measurement_1 = line[2]
        tmp.Measurement_2 = line[3]
        tmp.save()
    f.close()
