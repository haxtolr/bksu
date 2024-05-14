from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length=200)
    location_number = models.CharField(max_length=50)
    quantity = models.IntegerField()
    preview1 = models.CharField(max_length=200)
    volume = models.CharField(max_length=200)
    standard = models.CharField(max_length=200)
    special_standard = models.CharField(max_length=200)
    precision = models.CharField(max_length=200)
    is_defective = models.BooleanField()
    date_received = models.DateField()
    spare1 = models.CharField(max_length=200, blank=True, null=True)
    product_image = models.ImageField(upload_to='products/', blank=True, null=True)
    detail_image = models.ImageField(upload_to='details/', blank=True, null=True)
