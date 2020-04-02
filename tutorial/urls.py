from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from quickstart.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('activity_periods_api/',activity_periods_api),
    path('upload_csv/',upload_csv,name='upload_csv'),
]
# from django.db import models
# import uuid
# class Employee(models.Model):
#     id = models.CharField(max_length=100,primary_key=True, default=uuid.uuid4, editable=False)
#     real_name = models.CharField(max_length=20, null=True, blank=True)
#     tz = models.CharField(max_length=1000,default="Asia/Kolkata",null=True, blank=True)
#     def __str__(self):
#        return self.real_name

# class Activity_Periods(models.Model):       
#     employee = models.ForeignKey(Employee, null=True, blank=True, on_delete=models.CASCADE)   
#     start_date = models.DateTimeField(null=True, blank=True)
#     end_date = models.DateTimeField(null=True, blank=True)    

#     def __str__(self):
#        return str(self.start_date)+"To"+str(self.end_date)

# class Book(models.Model):
#     name = models.CharField(max_length=255)
#     isbn_number = models.CharField(max_length=13)
#     def __str__(self):
#         return self.name