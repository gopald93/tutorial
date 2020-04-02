from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from quickstart.models import *
from django.shortcuts import render, redirect
import csv
import pendulum
from datetime import datetime 
import json

def change_date_format(date_time_obj):
    required_data_obj = date_time_obj.strftime("%b %d %Y %I%p")
    return required_data_obj

def activity_periods_api(request):
    return_dict={}
    return_dict.update({"ok":True})
    return_dict.update({"members":[]})
    if request.method == 'GET': 
        employee_obj = Employee.objects.all()
        for data in employee_obj:
            demo_dict={}
            demo_dict.update({"id":data.id})
            demo_dict.update({"real_name":data.real_name})
            demo_dict.update({"tz":data.tz})
            demo_dict.update({"activity_periods":[]})
            for da in data.activity_periods_set.all():
                demo_dict_temp={}
                date_time_obj=change_date_format(da.start_date)
                demo_dict_temp.update({"start_date":date_time_obj})
                date_time_obj=change_date_format(da.end_date)
                demo_dict_temp.update({"end_date":date_time_obj}) 
                demo_dict.get("activity_periods").append(demo_dict_temp)
            return_dict.get("members").append(demo_dict)
        return JsonResponse(return_dict,safe=False)
    return JsonResponse({"message": "Hello, world!"},safe=False)

def get_time_zone():
    datetime_object = datetime.now()
    tz_type=pendulum.local(int(datetime_object.year),int(datetime_object.month),int(datetime_object.day))
    local_tz_name=tz_type.timezone.name
    print(local_tz_name)
    return local_tz_name

def create_employee_data(id,real_name,local_tz_name):
    emp_obj,emp_created=Employee.objects.get_or_create(id=id,real_name=real_name,tz=local_tz_name)
    return emp_obj,emp_created


def create_activity_periods(emp_obj,start_date,end_date):
    activity_period_obj,act_per_created=Activity_Periods.objects.get_or_create(employee=emp_obj,start_date=start_date,end_date=end_date)
    return activity_period_obj,act_per_created

def upload_csv(request):
    data={}
    local_tz_name=get_time_zone()
    if "GET" == request.method:
        return render(request, "quickstart/create_normal.html", data)
    else:    
        file = request.FILES["csv_file"] 
        decoded_file = file.read().decode('utf-8').splitlines()
        reader = csv.DictReader(decoded_file)
        check_id_available_list=[]
        for row in reader:
            if row.get("id") not in check_id_available_list:
                check_id_available_list.append(row.get("id"))
                emp_obj,created=create_employee_data(row.get("id"),row.get("real_name"),local_tz_name)
            start_time_obj = datetime.strptime(row.get("start_time"), '%Y/%m/%d %H:%M:%S')
            end_time_obj = datetime.strptime(row.get("end_time"), '%Y/%m/%d %H:%M:%S')
            activity_period_obj,act_per_created=create_activity_periods(emp_obj,start_time_obj,end_time_obj)
    return HttpResponse("Successfully upload the file")