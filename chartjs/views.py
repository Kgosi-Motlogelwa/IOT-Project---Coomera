from django.shortcuts import render
from django.conf import settings
# Working with Media file
import os
# Models
from .models import Imported_CSVs
from files.models import Document
# Chart
from django.views.generic import View   
from rest_framework.views import APIView
from rest_framework.response import Response 
from collections import defaultdict
# ======================================== #


# Homepage and fetches and processes files #
# ======================================== #
class HomeView(View): 
    def get(self, request, *args, **kwargs): 
        #Test variables
        repetition = "No Operation - For Repeated records" # are there any repeated data points
        test_files_1 = "No Operation - For Test if files exist" # are there any csv's
        test_files_2 = "No Operation - For Test if files is csv"
        date_test = "No Operation - Date Time conversion"
        # path to media file
        directory = 'media/media'

        # Itirate over files in media
        for filename in os.listdir(directory): 
            try:
                _f = os.path.join(directory, filename) 
                test_files_1 = 'Fetch/Concatonation from media file successful'
            except:
                test_files_1 = 'Fetch/Concatonation from media file failed'

            # Checking if it is a file 
            if os.path.isfile(_f) and '.csv' in _f: 
                test_files_2 = 'File is CSV'
                # Checking if it a CSV
                f = open(_f) 
                for line in f:
                        line =  line.split(',')
                        if Imported_CSVs.objects.filter(DateTime=line[1]).exists():
                            repetition = "Unsuccessful - All data repeated"
                        else:
                            repetition = "Success - Some new data added"
                            tmp = Imported_CSVs.objects.create()
                            tmp.Location = line[0]
                            # Sanetize DateTime
                            try:
                                tmp.DateTime = line[1]
                                #t = datetime.strptime(line[1], "%Y-%m-%d %H:%M:%S %p")
                                #tmp.DateTime = t.strftime("%Y-%m-%d %H:%M:%S %p")
                                date_test = "Date Time conversion worked"
                            except:
                                date_test = "Date Time failed to be cleaned"
                            tmp.Measurement_1 = line[2]
                            tmp.Measurement_2 = line[3]
                            tmp.save()
                f.close()
            else:
                test_files_2 = 'Problem with the File - may not be a CSV'

        context = {
            'repetition' : repetition,
            'test_files_1' : test_files_1,
            'test_files_2' : test_files_2,
            'date_test': date_test
        }
        return render(request, 'chartjs/index.html', context)

# Generate API to send #
#======================#
class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        # Import queryset of all objects and First Instance of each unique location.
        qs=Imported_CSVs.objects.all()
        qs_dist=Imported_CSVs.objects.distinct("Location").all()
        #
        # Variables to be export to template
        location_names = []
        location_data = []

        # Help - below loops
        iter = 0
        length = qs.count()
       
        for dist_loc_item in qs_dist:
            location_names.append(dist_loc_item.Location)
            # Temp use for each new location, fresh set to put in dict temp_dictionary
            # ======= #
            local_name = ''
            datetime_list = []
            measr1_list = []
            measr2_list = []
            # ======= #
            for item in qs:
                # Check if location matches, for lenth of queryset qs(All)
                if  dist_loc_item.Location == item.Location and iter < length:
                    local_name = item.Location
                    datetime_list.append(item.DateTime)
                    while 
                    if item.DateTime < start:
                        start = item.DateTime
                    if item.DateTime > end:
                        end = item.DateTime
                    measr1_list.append(item.Measurement_1)
                    measr2_list.append(item.Measurement_2)

            # Create a new dictionary to add into location_data
            temp_dictionary = {
                'Location': local_name,
                'Date_Time':datetime_list,
                'Measurement_1': measr1_list,
                'Measurement_2': measr2_list
            }
            location_data.append(temp_dictionary)

       
        userInput = "Green Forrest"
        datatime_list = []
        for item in location_data:
            if item['Location'] == userInput:
                location = item['Location']
                datatime_list = item['Date_Time'] 
                measr1_list = item['Measurement_1']
                measr2_list = item['Measurement_2']

        data = { 
            "location_names": location_names,
            "location": location,
            "datatime_list": datatime_list,
            "measr1_list": measr1_list,
            "measr2_list": measr2_list,
        }
        return Response(data)
