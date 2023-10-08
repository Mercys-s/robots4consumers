from django.shortcuts import render, redirect

from .models import Customer



def create_customer(request):

    if request.method == 'POST':
        email = request.POST["email"]
        customer_model = Customer.objects.create(email = email)
        customer_model.save()

        return redirect ('create_order')

    return render(request, 'customers/create_customer.html')



