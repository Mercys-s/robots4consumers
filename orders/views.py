from django.shortcuts import render

from .models import Order
from customers.models import Customer
from robots.models import Robot


def create_order(request):
    customer_models = Customer.objects.all() # - При большом объеме пользователей будет большая нагрузка, поэтому на 
    robot_models = Robot.objects.all()       #   на ходовом проекте email'ы будут получаться с request.user.email, 
                                             #   а не через весь список с БД
    context = {
        'customers': customer_models,
        'robots': robot_models,
    }

    if request.method == "POST":
        customer_obj = customer_models.filter(email = request.POST['customer']).get()
                                               
        new_order = Order.objects.create(customer = customer_obj, 
                                         robot_serial = request.POST['serial'])
        new_order.save()

    return render(request, 'orders/create_order.html', context)