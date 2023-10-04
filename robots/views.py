from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt

from .models import Robot

from time import strftime
import json


@csrf_exempt
def create_robots(request):

    if request.method == "POST":
        data = json.loads(request.body)
            
        v_data = validate_data(data) 
        robot = Robot.objects.create(serial = f'{v_data["model"]}-{v_data["version"]}', model = v_data["model"], \
                                     version = v_data["version"], created = v_data["created"])      
        robot.save()

    return render(request, 'robots/robots_created.html')


def validate_data(data):
    keys_list = [key for key in data] 

    for key in keys_list[:-1]:
        if len(data[key]) == 2:
            continue
        else:               
            raise ValueError('Модель и серия робота должна иметь по 2 символа!')

    if data["created"] == "":
        data["created"] = strftime('%Y-%m-%d %H:%M:%S')

    return data   
