from django.db import models

class Relative(models.Model):
    name = models.CharField(max_length=40)
    surname = models.CharField(max_length=20)
    age = models.IntegerField()
    address =models.CharField(max_length=40)
    celNum = models.IntegerField()
    email = models.EmailField()
    birthDayDate = models.DateField()
    hasEmigrated = models.BooleanField()