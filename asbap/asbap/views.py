from django.shortcuts import render
from asbap.billing.models import Customer


def customer_list(request):
    customers = Customer.objects.all()  # Query your Customer model to get a list of customers
    return render(request, 'billing/customer_list.html', {'customers': customers})
