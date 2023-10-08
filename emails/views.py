from django.shortcuts import render

from robots.models import Robot
from orders.models import Order

from django.dispatch import receiver, Signal

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

create_robot_signal = Signal()

@receiver(create_robot_signal, sender = Robot)
def send_email(robot, **kwargs):

    orders = Order.objects.filter(robot_serial = robot.serial)
    if orders:
        
        for order in orders:

            context = {'model': robot.model, 'version': robot.version}
            email = order.customer.email

            html_string = render_to_string('emails/email_template.html', context)

            message = EmailMultiAlternatives(subject = "Поступление новых роботов", to = [email,])
            message.attach_alternative(html_string, "text/html")
            message.send()

            orders.delete()