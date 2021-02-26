from adaptor.model import CsvModel
from adaptor.fields import CharField, FloatField, DateField
from django.db import models 
from django.contrib.auth.models import User

# Create your models here.
class Imported_CSVs(models.Model):
    Location = models.CharField(max_length=100000)
    DateTime = models.DateTimeField(blank=True, null=True)
    Measurement_1 = models.FloatField(blank=True, null=True)
    Measurement_2 = models.FloatField(blank=True, null=True)

# class myCsvModel(CsvModel):
#     Location = models.CharField(max_length=100000)
#     DateTime = models.DateTimeField()
#     Measurement_1 = models.FloatField()
#     Measurement_1 = models.FloatField()
#     class Meta:
#         dbModel = Imported_CSVs
#         delimiter = ","
       
#class Access_loc(models.Model):
    #location_id = models.CharField(max_length=100000)
    #user_1 = models.ForeignKey(User, related_name= "User 1")
