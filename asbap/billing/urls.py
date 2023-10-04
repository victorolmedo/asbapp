from django.urls import path
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'customers', views.CustomerViewSet)

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    #Clients
    path('addClient/', views.addClient, name='addClient'),
    path('listClients/', views.listClients, name='listClients'),

    #Products
    path('addProduct/', views.addProduct, name='addProduct'),
    path('listProducts/', views.listProducts, name='listProducts'),

    # invoices
    path('addInvoice/', views.addInvoice, name='addInvoice'),
    path('listInvoices/', views.listInvoices, name='listInvoices'),

    # Payments
    path('addPayment/', views.addPayment, name='addPayment'),
    path('listPayments/', views.listPayments, name='listPayments'),

    # vendors
    path('addVendor/', views.addVendor, name='addVendor'),
    path('listVendors/', views.listVendors, name='listVendors'),

    # Reports
    path('reports/', views.reports, name='reports'),

    # Settings
    path('settings/', views.settings, name='settings'),

]

