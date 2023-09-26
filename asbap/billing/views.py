from django.shortcuts import render
from django.http import HttpResponse

def BASE(request):
    return render(request, 'pages/base.html')

def dashboard(request):
    return render(request, 'pages/dashboard/index.html')

#Clients
def addClient(request):
    return render(request, 'pages/clients/addClient.html')
def listClients(request):
    return render(request, 'pages/clients/index.html')

#Products
def addProduct(request):
    return render(request, 'pages/products/addVendor.html')
def listProducts(request):
    return render(request, 'pages/products/index.html')

#invoices
def addInvoice(request):
    return render(request, 'pages/invoices/addInvoice.html')
def listInvoices(request):
    return render(request, 'pages/invoices/index.html')

#Payments
def addPayment(request):
    return render(request, 'pages/payments/addVendor.html')
def listPayments(request):
    return render(request, 'pages/payments/index.html')

#Vendors
def addVendor(request):
    return render(request, 'pages/vendors/addVendor.html')
def listVendors(request):
    return render(request, 'pages/vendors/index.html')

#Reports
def reports(request):
    return render(request, 'pages/reports/index.html')

#Settings
def settings(request):
    return render(request, 'pages/settings/index.html')

