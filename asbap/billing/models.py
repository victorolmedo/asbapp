from django.db import models

class Province(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)


class City(models.Model):
    name = models.CharField(max_length=100)
    provice_id = models.ForeignKey(Province, null=True, on_delete=models.SET_NULL)


class Customer(models.Model):
    first_name =models.CharField(max_length=100)
    last_name =models.CharField(max_length=100)
    email =models.CharField(max_length=100)
    address =models.CharField(max_length=100)
    ruc =models.CharField(max_length=100)
    document_number =models.CharField(max_length=100)
    phone =models.CharField(max_length=100)
    image_path =models.CharField(max_length=100)
    birthday =models.DateField()
    active =models.BooleanField()
    person_type =models.CharField(max_length=20)
    city_id =models.ForeignKey(City, null=True, on_delete=models.SET_NULL)
    user_id =models.IntegerField()
