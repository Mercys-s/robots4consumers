from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt

from .models import Robot

from .excel import info_to_excel

from emails.views import create_robot_signal

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

        info_to_excel('.//robots//static//robots//documents//robots.xlsx', v_data, Robot)

        create_robot_signal.send(sender = Robot, robot = robot)

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
