from django.db import models
import uuid
import pytz
def create_time_zone():
    main_time_zone_list=[]
    for tz in pytz.all_timezones:
        demo_data=(tz,tz)
        main_time_zone_list.append(demo_data)
    return  main_time_zone_list   

class Employee(models.Model):
    id = models.CharField(max_length=100,primary_key=True)
    real_name = models.CharField(max_length=20, null=True, blank=True)
    tz = models.CharField(max_length=1000,choices=create_time_zone(),default="Asia/Kolkata",null=True, blank=True)
    def __str__(self):
       return self.real_name

class Activity_Periods(models.Model):       
    employee = models.ForeignKey(Employee, null=True, blank=True, on_delete=models.CASCADE)   
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)    

    def __str__(self):
       return str(self.start_date)+"To"+str(self.end_date)

class Book(models.Model):
    name = models.CharField(max_length=255)
    isbn_number = models.CharField(max_length=13)
    def __str__(self):
        return self.name