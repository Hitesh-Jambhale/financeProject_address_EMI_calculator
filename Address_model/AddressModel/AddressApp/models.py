from django.db import models

# Create your models here.

class PermanentAddress(models.Model):
    flat_no = models.IntegerField()
    street_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pincode = models.IntegerField()
    area = models.CharField(max_length=100)
    landmark = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.flat_no

class CurrentAddress(models.Model):
    Cflat_no = models.IntegerField()
    Cstreet_name = models.CharField(max_length=100)
    Ccity = models.CharField(max_length=100)
    Cpincode = models.IntegerField()
    Carea = models.CharField(max_length=100)
    Clandmark = models.CharField(max_length=100)
    Cdistrict = models.CharField(max_length=100)
    Cstate = models.CharField(max_length=100)
    Ccountry = models.CharField(max_length=100)

    def __str__(self):
        return self.flat_no

