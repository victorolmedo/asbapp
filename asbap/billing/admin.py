from django.contrib import admin
from .models import City, Province, Customer

# Register your models here.
admin.site.register(Customer)
admin.site.register(Province)
admin.site.register(City)
